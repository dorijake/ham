from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

	SEX_CHOICES = (
		("M", "Male"),
		("W", "Female"),
	)

	phone = models.CharField(max_length=11, unique=True)
	img = models.CharField(max_length=255, null=True, blank=True)
	is_owner = models.BooleanField(default=0)
	location1 = models.CharField(max_length=20, null=True, blank=True)
	location2 = models.CharField(max_length=20, null=True, blank=True)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="M")

	username = models.CharField(max_length=30, unique=True)
		

# status of a relationship
class Friends_Status(models.Model):
	code = models.CharField(max_length=3, unique=True)
	name = models.CharField(max_length=200, unique=True)


class Friends(models.Model):
	user = models.ForeignKey(User, related_name='user_list')
	friend = models.ForeignKey(User, related_name='friend_list')
	action_user = models.ForeignKey(User, related_name='action_user')
	status = models.ForeignKey(Friends_Status, to_field='code')

	class Meta:
		unique_together = ('user', 'friend',)