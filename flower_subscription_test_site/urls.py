from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from signup.views import signup_list
from signup.views import SignupCreate	
from . import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flower_subscription_test_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomepageView.as_view(), name='home'),
    # url(r'^signup_list/$', signup_list, name='signup_list'),
    url(r'^signup/$', SignupCreate.as_view(), name='signup'),

    url(r'^admin/', include(admin.site.urls)),
)
