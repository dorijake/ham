from django.conf.urls import url
from graph import views

urlpatterns = [
    url(r'^$', views.graphtest, name='graphtest'),
]