from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forums/$', views.post_list, name='post_list'),
    url(r'^forums/(?P<post_id>\d+)/[\s\S]*', views.detail, name='detail'),
]