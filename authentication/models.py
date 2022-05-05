from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    frname = models.CharField(max_length=30, default="")
    birthday = models.CharField(max_length=20, default="")
    address1 = models.CharField(max_length=50, default="")
    address2 = models.CharField(max_length=50, default="")
    code = models.CharField(max_length=5)
    phone = models.CharField(max_length=30)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)