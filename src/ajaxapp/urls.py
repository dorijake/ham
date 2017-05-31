# from django.conf.urls import url
# from ajaxapp import views
 
# urlpatterns = [
#     # url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
#     url(r'^$', views.2ndex, name='aaa')
# ]

from django.conf.urls import url
from ajaxapp import views

urlpatterns = [
    url(r'^aaa/$', views.SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]