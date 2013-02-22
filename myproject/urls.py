from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
#Url creada para decirle al sistema donde buscar los archivos subidos
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, }
    ),
)


urlpatterns = patterns('myproject.views',
    url(r'^$', 'index'),
)


# Esta linea hace que en modo produccion o trabajando con el wsgi funcionen
# los static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
