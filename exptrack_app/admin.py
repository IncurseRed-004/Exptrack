from django.contrib import admin
from django.contrib.auth.models import User

from exptrack_app.models import Profile, Login, Category, Expense

# Register your models here.

admin.site.register(Login)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Expense)