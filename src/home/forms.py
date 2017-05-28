from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from user.models import User

class UserCreationForm(UserCreationForm):
 
    # phone = forms.CharField(
    #     max_length=User._meta.get_field('phone').max_length,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'form-control',
    #             'required':'True',
    #             'autocomplete':'off',
    #         })
    # )


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        # common widget attributes for all fields in the form
        
        attrs = {'class':'form-control', 'autocomplete':'off'}

        # key is a field name and value is a Field class
        for key, field in self.fields.items():
            field.help_text = None
            attrs.update({'placeholder':key})
            field.widget.attrs.update(attrs)

        
        print(self.base_fields.keys())
 
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone', 'sex')



class AuthenticationForm(AuthenticationForm):
	username = forms.CharField(label="ID", max_length=30, widget=forms.TextInput())
	