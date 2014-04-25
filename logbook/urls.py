from django.conf.urls import patterns, url

from logbook import views

urlpatterns = patterns('',
	url(r'^$', views.LatestView.as_view(), name='latest'),
	url(r'^(?P<pk>\d+)/$', views.RouteView.as_view(), name='route'),
	url(r'^route_entry/$', views.new_route_and_climb, name='new_route'),
	url(r'^route_entry/(?P<crag_id>\d+)/$', views.new_route_at_crag, name='new_route_at_crag'),
	url(r'^log_climb/$', views.log_climb, name='log_climb'),
	url(r'^thanks/$', views.thanks, name='thanks'),
	url(r'^choose_crag/$', views.CragView.as_view(), name='choose_crag'),
)
