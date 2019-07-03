# Simple & Co
_Simple & Co_ คือระบบร้านขายเสื้อผ้า โดยผู้ใช้สามารถทำการสร้าง Product, Order และสามารถเรียกดู Total Income ได้ 
หน้าที่ของคุณคือการทำระบบตัวนี้ให้สมบูรณ์

**กรุณาอ่านเอกสารนี้ให้จบก่อนเริ่มทำแบบทดสอบ** หากมีข้อสงสัยกรุณาสอบถามผ่านทางอี-เมล ```job@thegang.tech```

## Project Information
Simple & Co เป็น Rest API Server ที่ใช้ Django Rest Framework เป็นหลัก รูปแบบของโปรเจ็คจะอยู่ในรูปแบบโปรเจ็คของ 
Django ทั่วไป โดยแอพพลิเคชั่นที่คุณต้องแก้ไขคือ แอพ ``shop`` 

เราใช้ ```pipenv``` ในการเช็ต environment ของ python

## Exercises
เราได้เขียน ``shop/tests.py`` ไว้ หน้าที่ของคุณคือเขียนโค้ดเพิ่มเติมเพื่อให้ test ผ่าน และมีความถูกต้องมากที่สุด

สิ่งที่คุณต้องทำหลักมีดังนี้
1. สร้าง Model ``Order`` _(ให้อ่านจาก ```shop/tests.py``` ว่า model ควรมี field และ relation อะไรบ้าง)_
2. สร้าง REST Endpoint สำหรับ Model ``Order``
3. ทำ Logic ในการคำนวน Total ของ Order นั้นๆ โดยการบวกราคาของสินค้าใน Order และลบ discount
4. สร้าง Endpoint สำหรับการดู Total income โดยการรวมรายได้จาก Order ที่มี State เป็น Done

หากคุณทำแบบทดสอบถูกต้อง คุณต้องสามารถรัน test โดยใช้ ```python manage.py test``` และผ่านทั้งหมด

## Rules
เราคาดหวังว่าคุณจะสามารถทำแบบทดสอบให้ผ่านได้ทั้งหมด และโค้ดที่คุณเขียนเพิ่มขึ้นมานั้น มีความสะอาด เข้าใจง่าย และมีความถูกต้อง

คุณสามารถ
 * แก้ไขโค้ดทั้งหมด ยกเว้นไฟล์ ```shop/tests.py```
 * เพิ่ม / ลบ package
 * [Duplicate repo](https://help.github.com/en/articles/duplicating-a-repository) ตัวนี้เข้า private repo เพื่อทำแบบทดสอบ
 
คุณห้าม
 * แก้ไขไฟล์ ```shop/tests.py```
 * ให้ผู้อื่นทำแบบทดสอบให้
 * ลอกแบบทดสอบจากผู้อื่น
 * อัพโหลดคำตอบแบบทดสอบขึ้น public website
 
 ## About
 ระบบตัวนี้เป็นแบบทดสอบสำหรับผู้ที่สนใจสมัครเข้าทำงาน Junior Backend Developer ที่ [The Gang Technology](https://thegang.tech)
 
 หากคุณสนใจสมัครในตำแหน่งนี้ ให้ทำแบบทดสอบตัวนี้ให้เสร็จเรียบร้อย โดย
 1. [Duplicate repo](https://help.github.com/en/articles/duplicating-a-repository) ตัวนี้ไปที่ Private Github Repo ของคุณ
 2. ทำการเพิ่ม access ของ repo โดยการใช้ ```job@thegang.tech```
 3. ส่ง Resume พร้อมแนะนำตัวคุณ แบบสั้นๆมาที่ ```job@thegang.tech```