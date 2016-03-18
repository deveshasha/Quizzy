from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
	
	url(r'^$',views.test,name='index'),
	url(r'ctest/$', views.index, name='index'),
	url(r'ctest/result/$',views.result, name='result'),
]