"""
URL configuration for todoapplication project.

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
from django.urls import path,include
from reminderapp.views import RegisterView,LoginView,HomeView,TodoDeleteView,TodoUpdateView,SignOutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView.as_view(),name='register'),
    path('signin/',LoginView.as_view(),name='login'),
    path('',HomeView.as_view(),name='home'),
    path('todos/<int:pk>/remove',TodoDeleteView.as_view(),name='todo_delete'),
    path('todos/<int:pk>/change',TodoUpdateView.as_view(),name='todo_update'),
    path('signout/',SignOutView.as_view(),name='signout'),
    path('api/',include('api.urls'))
]
