from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

# User model Manager
class UserManager(UserManager):
	
	def get_friends(self, id):
		user_info = self.filter(id=id).prefetch_related('user1_set', 'user2_set')

		friend_list = user_info.annotate(friend_id=F('user1_set__user2'), friend_name=F('user1_set__user2__username')).exclude(
				friend_id__isnull=True, friend_name__isnull=True).values('friend_id', 'friend_name').union(
				user_info.annotate(friend_id=F('user2_set__user1'), friend_name=F('user2_set__user1__username')).exclude(
				friend_id__isnull=True, friend_name__isnull=True).values('friend_id', 'friend_name'))

		
		return friend_list

class User(AbstractUser):

	SEX_CHOICES = (
		("M", "Male"),
		("W", "Female"),
	)

	username = models.CharField(max_length=20, unique=True)
	phone = models.CharField(max_length=11, unique=True)
	img = models.CharField(max_length=255, null=True, blank=True)
	is_owner = models.BooleanField(default=0)
	location1 = models.CharField(max_length=20, null=True, blank=True)
	location2 = models.CharField(max_length=20, null=True, blank=True)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="M")
	
	objects = UserManager()	


# status of a relationship
class Friends_Status(models.Model):
	code = models.CharField(max_length=3, unique=True, primary_key=True)
	name = models.CharField(max_length=200, unique=True)



class Friends(models.Model):
	user1 = models.ForeignKey(User, related_name='user1_set')
	user2 = models.ForeignKey(User, related_name='user2_set')
	action_user = models.ForeignKey(User, related_name='action_user')
	status = models.ForeignKey(Friends_Status, to_field='code')
	
	class Meta:
		unique_together = ('user1', 'user2',)



