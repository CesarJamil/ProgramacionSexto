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
	url(r'^flot/$', views.flot),
	url(r'^morris/$', views.morris),
	url(r'^inline/$', views.inline),
	url(r'^buttons/$', views.buttons),
	url(r'^general/$', views.general),
	url(r'^icons/$', views.icons),
	url(r'^modals/$', views.modals),
	url(r'^sliders/$', views.sliders),
	url(r'^timeline/$', views.timeline),
	url(r'^generalElements/$', views.generalElements),
	url(r'^advanced/$', views.advanced),
	url(r'^editors/$', views.editors),
	url(r'^simple/$', views.simple),
	url(r'^data/$', views.data),
	url(r'^invoice/$', views.invoice),

]
