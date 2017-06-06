from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home.forms import UserCreationForm
from .models import User

class UserAdmin(UserAdmin):
	add_form = UserCreationForm
	

	add_fieldsets = (
		(None, {
			'fields': ('username', 'password1', 'password2', 'phone', 'sex',)
		}),
	)

UserAdmin.list_display += ('phone',)
UserAdmin.list_filter += ('phone',)
UserAdmin.fieldsets[1][1]['fields'] += ('phone',)

admin.site.register(User, UserAdmin)
