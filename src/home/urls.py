from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views, forms

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'signup/$', views.signup, name='signup'),
	url(r'signup/extra_info/(?P<userid>\d+)/$', views.extra_info, name='extra_info'),
	url(r'signup/done', views.signup_done, name='signup_done'),
	url(r'login/$', auth_view.login,
		{'authentication_form':forms.AuthenticationForm, 'template_name':'home/login.html',}, name='login'),
	url(r'logout/$', auth_view.logout, {'template_name':'home/index.html',}, name='logout'),
]