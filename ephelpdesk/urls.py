from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name='logout'),
    url(r'', include('helpdesk.urls', namespace='helpdesk')),
    ]
