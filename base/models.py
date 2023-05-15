from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    # Add name field to the user model
    name = models.CharField(max_length=200, null=True)
    # Add ip_address field to the user model
    ip_address = models.GenericIPAddressField(unique=False, default='0.0.0.0')
    # Add created field to the user model with auto_now_add set to True
    created = models.DateTimeField(auto_now_add=True)
    # Remove email field from required fields
    REQUIRED_FIELDS = []

class Data_Sent(models.Model):
    # Add created field to the Data_Sent model with auto_now_add set to True
    created = models.DateTimeField(auto_now_add=True)
    # Add data field to the Data_Sent model with JSONField data type
    data = models.JSONField()
    # Add user field to the Data_Sent model as a foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Return the string representation of created field when Data_Sent object is printed
        return str(self.created)
