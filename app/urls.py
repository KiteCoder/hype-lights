from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from app import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# App imports
from mobile import views as mobile_views
from designer import views as designer_views
from account import views as account_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),


    # Account webpages

    # url(r'^account/login/$', account_views.login, name='login'), #very basic function, not real login yet
    url(r'^account/index/$', account_views.index, name='index'),
    url(r'^index/$', account_views.index, name='index'),
    url(r'^$', account_views.index, name='index'),
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^logout_view/$', account_views.logout_view, name='logout_view'),


    # Mobile Endpoints
    url(r'^mobile/pattern_request', mobile_views.get_config_json, name='get_config_json'),



    # Designer Endpoints
    url(r'^designer/create_show', designer_views.create_show, name='create_show'),
    url(r'^designer/create_frame', designer_views.create_frame, name='create_frame'),
    url(r'^designer/create_grid', designer_views.create_grid, name='create_grid'),
    url(r'^designer/create_pixel', designer_views.create_pixel, name='create_pixel'),
    url(r'^designer/create_framepixel', designer_views.create_framepixel, name='create_framepixel'),
    url(r'^designer/parse', designer_views.path_extracter, name='path_extracter'),



    # Designer webpages
    url(r'^create/$', designer_views.create, name='create'),
    url(r'^render_frame/(?P<frame_id>\w+)', designer_views.render_frame, name='render_frame'),
    

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
