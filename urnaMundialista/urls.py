from django.conf.urls import url
from urnaMundialista import views, models
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.base), name='base'),
    url(r'^jugador/$', views.JugadorListView.as_view(), name='jugadores-list'),
    url(r'^jugador/(?P<pk>\d+)/detail/$', views.JugadorDetailView.as_view(), name='jugadores-detail'),
    url(r'^jugador/(?P<pk>\d+)/update/$', views.JugadorUpdate.as_view(),name='jugadores-update'),
    #Create
    url(r'^jugadores/create/$', views.JugadorCreate.as_view(), name='jugadores-create'),
    #Delete
    url(r'^jugadores/(?P<pk>\d+)/delete/$', views.JugadorDelete.as_view(), name='jugadores-delete'),
]