from django.db import models

# Create your models here.
class Register_Master(models.Model):
    Reg_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=40,unique=True)
    Mob=models.CharField(max_length=30) 
    Password=models.CharField(max_length=30)
    DOB=models.DateField(default=None)
    Gender=models.CharField(max_length=40)
    Address=models.CharField(max_length=100)
    Role_name=models.CharField(max_length=30)
    Status=models.IntegerField(default=0)
    def __str__(self):
        return self.Name