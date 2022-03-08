from django.conf.urls import url
from django.views.generic import RedirectView

from . import views



app_name = 'extempore'
urlpatterns = [
	url(r'^search.html$', views.search, name='search', kwargs={'page': "search"}),
	# custom Extempore source  views
	url(r'^def/(?P<permalink>.+)$', views.funpage, name='fun_detail'),
	url(r'^index/core$', views.index, name='list_core', kwargs={'page': "core"}),
	url(r'^index/extras$', views.index, name='list_custom', kwargs={'page': "extras"}),
	url(r'^$', RedirectView.as_view(url='/index/core'), name="home"),


]
	
