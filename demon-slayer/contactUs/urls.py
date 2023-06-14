from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="indexh"),
    path('hashiras/', include('hashira.urls'), name='hashiras'),
    path('lowermoon/', include('demons.urls'), name='demons'),
    path('reg/', views.reg , name='reg'),
]
