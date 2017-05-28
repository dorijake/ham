from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'friends/', views.friend_list, name='friends'),
]