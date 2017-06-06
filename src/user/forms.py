from django import forms
from .models import Friends, User


class FriendsForm(forms.ModelForm):

	class Meta:
		model = Friends
		fields = '__all__'


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['location1', 'location2']