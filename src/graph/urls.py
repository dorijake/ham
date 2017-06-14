<<<<<<< HEAD
from django.conf.urls import url
from graph import views

urlpatterns = [
    url(r'^$', views.graphtest, name='graphtest'),
    url(r'^aa/$', views.get_f2p_graph, name='get_f2p_graph'),
=======
from django.conf.urls import url
from graph import views

urlpatterns = [
    url(r'^$', views.graphtest, name='graphtest'),
    url(r'^aa/$', views.get_f2p_graph, name='get_f2p_graph'),
>>>>>>> ca7662ff2d0d75ce2e303722302ebb37c6ac3b59
]