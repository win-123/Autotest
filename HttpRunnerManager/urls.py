"""HttpRunnerManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import include
from django.urls import re_path
from django.views.generic import RedirectView

from HttpRunnerManager.activator import process
from ApiManager import views
import xadmin

urlpatterns = [
    re_path('^api/login/', views.login),
    re_path('^xadmin/', xadmin.site.urls),
    re_path('^favicon\.ico$', RedirectView.as_view(url='/static/assets/img/favicon.ico')),
    re_path('^(?P<app>(\w+))/(?P<function>(\w+))/$', process),
    re_path('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\w+))/$', process),

]
