from django.db import models
import datetime
# Create your models here.
#admin model
"""class Hotels(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=20)
    contact_no=models.IntegerField()"""
#===================================
class Room(models.Model):
    room_type=models.CharField(max_length=50)
    max_numbers=models.IntegerField()
    bed_option=models.CharField(max_length=50)
    price=models.IntegerField()
    total_rooms=models.CharField(max_length=50)
    date=models.DateField()
 #=============================================
class Review(models.Model):
     #user=models.ForeignKey(User,on_delete=models.CASCADE)
     comment=models.CharField(max_length=255)
     rating=models.IntegerField()
     created_at=models.DateField()
     updated_at=models.DateField()
#====================================================
class Check_Availability(models.Model):
    room_type=models.ForeignKey(Room,on_delete=models.CASCADE)
    maxno=models.CharField(max_length=10)
    check_In=models.DateField()
    check_Out=models.DateField()
#============================================
class UserRegister(models.Model):
    fname=models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email_id=models.EmailField(max_length=20,primary_key=True)
    password=models.CharField(max_length=50)
    rpassword = models.CharField(max_length=50)
    contact_no=models.IntegerField()
    address=models.CharField(max_length=100)
'''User Model
class Check_Availability(models.Model):
    room_type=models.IntegerField()
    maxno=models.CharField(max_length=10)
    check_In=models.DateField()
    check_Out=models.DateField()
class Reserve_Room(models.Model):
    room_no=models.IntegerField(max_length=50,primary_key=True)
    room_type=models.ForeignKey(Check_Availability,on_delete=models.CASCADE)
    credit_card=models.IntegerField()
    debit_card=models.IntegerField()
    check_In=models.DateField()
    check_Out=models.DateField()
class Display(models.Model):
    user_name=models.CharField(max_length=50)
    cust_id=models.IntegerField()
    room_type=models.CharField(max_length=50,primary_key=True)
    room_no=models.ForeignKey(Reserve_Room,on_delete=models.CASCADE)
    check_In=models.DateField()
    check_Out=models.DateField()
    total_cost=models.FloatField()
class Cancle_Room(models.Model):
    user_name=models.CharField(max_length=50)
    room_no=models.ForeignKey(Display,on_delete=models.CASCADE)
    cust_id=models.IntegerField()'''


