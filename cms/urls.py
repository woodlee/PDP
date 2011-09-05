from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', 
		{ 'document_root': '/Users/woodlee/Dev/tinymce/jscripts/tiny_mce' }),
	url(r'^search/$', 'cms.search.views.search'),
    url(r'', include('django.contrib.flatpages.urls')),
)
