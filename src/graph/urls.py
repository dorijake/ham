from django.conf.urls import url
from graph import views

urlpatterns = [
    url(r'^$', views.graphtest, name='graphtest'),
    url(r'^aa/$', views.get_f2p_graph, name='get_f2p_graph'),
]