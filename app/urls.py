from django.conf.urls import include, url
from django.contrib import admin

# App imports
from mobile import views as mobile_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    # Mobile Endpoints
    url(r'^mobile/pattern_request', mobile_views.get_config_json, name='get_config_json'),

]
