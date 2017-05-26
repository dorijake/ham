from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
	phone = models.CharField(max_length=13, unique=True)
	img = models.CharField(max_length=255, null=True, blank=True)
	is_owner = models.BooleanField(default=0)

	