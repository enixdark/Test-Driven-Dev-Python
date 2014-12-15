from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TDD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include("app.lists.urls")),

)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
