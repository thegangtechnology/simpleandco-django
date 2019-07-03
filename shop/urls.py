from rest_framework import routers

from shop.views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
urlpatterns = router.urls

urlpatterns += [
]
