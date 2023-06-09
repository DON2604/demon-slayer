"""
URL configuration for ds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="indexh"),
    path('hashiras/', include('hashira.urls'), name='hashiras'),
    path('lowermoon/', include('demons.urls'), name='demons'),
    path('reg/', views.reg , name='reg'),
    path('signup', views.accr , name='accr'),
    path('login', views.accin,  name="accin"),
    path('logout', views.accout , name="accout"),
    path('contactUs/',include('contactUs.urls'),name="contact"),
    path('spotlight/', include('spotlight.urls'), name='spotlight'),

]


