from django.db import models

# Create your models here.
class Create_Acc(models.Model):
    sno=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=200,default='')
    Password=models.CharField(max_length=200)
    Email_id=models.CharField(max_length=200,unique=True,default='')
    Mobile=models.CharField(max_length=200,unique=True)