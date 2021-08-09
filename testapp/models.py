import uuid
from django.contrib.auth.hashers import check_password, make_password

from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField()
    password = models.CharField(max_length=254)

    def __str__(self):
        return self.email
    
    def create_user(self, email, pwd):
        self.email = email
        self.password = self.make_password(pwd)
        self.save()
        return self
    
    def check_user(self, pwd):
        if self.check_password(pwd):
            return self
        return None

    def make_password(self, password):
        return make_password(password)
    
    def check_password(self, password):
        encoded = self.password
        return check_password(password, encoded)

class BPI(models.Model):

    code = models.CharField(max_length=50)
    symbol = models.CharField(max_length=100)
    rate = models.FloatField()
    description = models.CharField(max_length=254)
