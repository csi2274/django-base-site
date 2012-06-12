"""
Add any additional URLs that should only be available when using the the
settings.development configuration.

See ``urls.defaults`` for a list of all URLs available across both
configurations.
"""
from .defaults import *

# Debug/Development URLs
if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    )
