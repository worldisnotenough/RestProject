from django.conf.urls import patterns, url
from RestApp import myviews

from rest_framework.urlpatterns import format_suffix_patterns

from RestApp import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_view, name='index_view'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', myviews.Register.as_view(),name='register'),
   # url(r'^register/$',myviews.register,name='register'),
)

urlpatterns = format_suffix_patterns(urlpatterns)