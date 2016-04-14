from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
	
	url(r'^$',views.test),
	url(r'jtest/$', views.javaindex),
	url(r'jtest/result/$',views.javaresult),
	url(r'phptest/$', views.phpindex),
	url(r'phptest/result/$',views.phpresult),
]