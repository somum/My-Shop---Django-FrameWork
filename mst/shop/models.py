from django.db import models
from datetime import datetime
# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images",default="")
    pub_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name


class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,default="")
    password=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.username


class userInformation(models.Model):
    userInformation_id=models.AutoField(primary_key=True)
    userfull_name=models.CharField(max_length=100,default="")
    phone_no=models.CharField(max_length=50,default="")
    user_email=models.CharField(max_length=50,default="")
    user_company=models.CharField(max_length=50,default="")
    user_position=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.userfull_name