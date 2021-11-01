from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('impromptu.views',

	url(r'^filebrowser$', 'filebrowser', name='filebrowser'),

		
	# NEW..
	
	url(r'^(?P<num>.+)$', 'funpage', name='impromptu_fun_detail'),
		
	url(r'^$', 'index', name='impromptu_home'),
	
)

