from django.db.models import Model
from django.db import models
from django.contrib.auth.models import AbstractUser

class LoginModel(Model):
    username=models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    role=models.CharField(max_length=50,default="")
    status = models.CharField(max_length=50, default="")

class UserModel(Model):
    name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    class Meta:
        db_table = "users"

class MedicineModel(Model):

    name= models.CharField(max_length=500)
    symptoms= models.CharField(max_length=500)
    disease= models.CharField(max_length=500)
    count= models.CharField(max_length=500)
    price= models.CharField(max_length=500)
    alternates= models.CharField(max_length=500)
    username= models.CharField(max_length=500)

class ReviewModel(Model):

    medicine= models.CharField(max_length=500)
    review= models.CharField(max_length=500)
    user= models.CharField(max_length=500)
    date= models.CharField(max_length=500)