import random
from decimal import Decimal
from random import randrange

from hypothesis import given
from hypothesis.strategies import text, decimals, characters
from hypothesis.extra.django import TestCase
from rest_framework.test import APITestCase, APIRequestFactory

from shop.models import Order, Product
from shop.serializers import ProductSerializer


class TestShopMigration(TestCase, APITestCase):

    _NAME = text(min_size=1, max_size=42, alphabet=characters(whitelist_categories=('Lu', 'Ll')))
    _CONTENT = text(min_size=1, alphabet=characters(whitelist_categories=('Lu', 'Ll')))
    _PRICE = decimals(places=2, min_value=0, max_value=20000000, allow_nan=False, allow_infinity=False)
    _DISCOUNT = decimals(places=2, min_value=0, max_value=30, allow_nan=False, allow_infinity=False)

    def create_product(self, name, content, price):
        data = {
            "name": name,
            "content": content,
            "price": price
        }
        response = self.client.post("/shop/products/", data)
        self.assertIsNotNone(response.data["url"])
        self.assertIs(response.status_code, 201)

    @given(_NAME,
           _CONTENT,
           _PRICE)
    def test_create_product(self, name, content, price):
        self.create_product(name, content, price)

    def test_create_order(self):
        number_of_product = randrange(1, 10)
        [self.create_product(self._NAME.example(), self._CONTENT.example(), self._PRICE.example()) for _ in range(number_of_product)]
        products = Product.objects.all()[:number_of_product]
        factory = APIRequestFactory()
        request = factory.get("/")
        products_list = [ProductSerializer(product, context={'request': request}).data['url'] for product in products]
        data = {
            "ref_no": self._NAME.example(),
            "customer_name": self._NAME.example(),
            "products": products_list,
            "discount": self._DISCOUNT.example()
        }

        response = self.client.post("/shop/orders/", data)
        self.assertIs(response.status_code, 201)
        self.assertIsNotNone(response.data["url"])
        self.assertIs(response.data["state"], Order.PENDING)
        return response.data["url"]

    def test_order_total_calculation(self):
        number_of_product = randrange(1, 10)
        [self.create_product(self._NAME.example(), self._CONTENT.example(), self._PRICE.example()) for _ in range(number_of_product)]
        products = Product.objects.all()[:number_of_product]
        factory = APIRequestFactory()
        request = factory.get("/")
        products_list = [ProductSerializer(product, context={'request': request}).data['url'] for product in products]
        discount = self._DISCOUNT.example()
        data = {
            "ref_no": self._NAME.example(),
            "customer_name": self._NAME.example(),
            "products": products_list,
            "discount": discount,
            "total": 0
        }

        total_should_be = sum([p.price for p in products]) - discount

        response = self.client.post("/shop/orders/", data)
        self.assertIs(response.status_code, 201)
        self.assertEqual(Decimal(response.data["total"]), total_should_be)
        return response.data["url"]

    def change_order_state(self, data_url, state):
        data = self.client.get(data_url)
        data.data["state"] = state
        del data.data["ref_no"]
        del data.data["customer_name"]
        del data.data["discount"]
        del data.data["products"]
        response = self.client.patch(data_url, data.data)
        self.assertIs(response.status_code, 200)

    def test_list_orders(self):
        [self.create_product(self._NAME.example(), self._CONTENT.example(), self._PRICE.example()) for _ in range(5)]
        response = self.client.get("/shop/orders/")
        self.assertIsNotNone(response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_orders(self):
        order = self.test_create_order()
        response = self.client.delete(order)
        self.assertEqual(response.status_code, 204)

    def test_calculate_income(self):
        orders = [self.test_create_order() for _ in range(20)]
        total_income = Decimal(0.0)
        for order in orders:
            choice = random.choice([Order.CONFIRM, Order.DONE])
            if choice is Order.DONE:
                data = self.client.get(order)
                total_income += Decimal(data.data["total"])
            self.change_order_state(order, choice)

        response = self.client.get("/shop/reports/total_income")
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.data["total_income"], total_income)
