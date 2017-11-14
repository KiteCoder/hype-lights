from django.conf.urls import include, url
from django.contrib import admin

# App imports
from mobile import views as mobile_views
from designer import views as designer_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    # Mobile Endpoints
    url(r'^mobile/pattern_request', mobile_views.get_config_json, name='get_config_json'),



    # Designer Endpoints
    url(r'^designer/create_show', designer_views.create_show, name='create_show'),
    url(r'^designer/create_frame', designer_views.create_frame, name='create_frame'),
    url(r'^designer/create_grid', designer_views.create_grid, name='create_grid'),
    url(r'^designer/create_pixel', designer_views.create_pixel, name='create_pixel'),
    url(r'^designer/create_framepixel', designer_views.create_framepixel, name='create_framepixel'),

]
