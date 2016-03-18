"""DDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from polls.views import *
from login.views import *
from . import views


urlpatterns = [
    #url(r'^test/ctest/$',views.index),
    #url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', user_login),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^register/success/', views.register_success),
    url(r'^$', views.home),
    #url(r'^test/',include('polls.urls')),
    url(r'^test/',views.test),
    url(r'^ctest',index),
    url(r'^result',result),
    url(r'^contact',contact),

]
