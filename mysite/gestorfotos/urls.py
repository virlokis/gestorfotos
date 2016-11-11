from django.conf.urls import url

from . import views

app_name = 'gestorfotos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<evento_id>[0-9]+)/$', views.evento, name='evento'),
]
