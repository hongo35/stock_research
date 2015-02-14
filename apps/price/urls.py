from django.conf.urls import patterns, url

from stock_research.price import views

urlpatterns = patterns('',
	# ex: /price/
	url(r'^$', views.index, name='index'),
	# ex: /price/1301/
	url(r'^(?P<ccode>\d+)/$', views.detail, name='detail'),
)
