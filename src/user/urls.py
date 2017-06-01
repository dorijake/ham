from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'friends/$', views.friend_list, name='friends'),
	url(r'friends/search/', views.search_user, name='search_user'),
	url(r'friends/add/', views.add_friend, name='add_friend'),
	url(r'friends/delete/', views.delete_friend, name='delete_friend'),
]