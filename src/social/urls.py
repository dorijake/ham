from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'', views.main, name='social_main'),
	url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]