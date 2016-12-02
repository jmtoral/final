from django.conf.urls import url

from . import views

app_name = 'maps'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.embedded_map, name = 'map'),
]
