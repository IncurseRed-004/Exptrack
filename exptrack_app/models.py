from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile_pics", blank=True)


class Profile(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name ="profile")
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Category(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name ="categories")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name ="expenses")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name ="expenses")
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title