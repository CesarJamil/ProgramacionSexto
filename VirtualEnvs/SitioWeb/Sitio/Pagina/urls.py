from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.mostrar_inicio),
	url(r'^ventana2/$', views.widgets),
	url(r'^ventana3/$', views.calendar),
]