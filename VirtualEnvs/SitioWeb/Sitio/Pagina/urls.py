from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.mostrar_inicio),
	url(r'^ventana2/$', views.widgets),
	url(r'^ventana3/$', views.calendar),
	url(r'^dashboardv2/$', views.dashboardv2),
	url(r'^topNav/$', views.topNav),
	url(r'^boxed/$', views.boxed),
	url(r'^fixed/$', views.fixed),
	url(r'^collapsedSidebar/$', views.collapsedSidebar),
	url(r'^chartjs/$', views.chartjs),
]
