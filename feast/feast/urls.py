"""feast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from culinary_guide import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
]
urlpatterns += [
    path('', views.index, name='home'),
    path('first_meal', views.first_meal, name='first_meal'),
    path('main_dishes', views.main_dishes, name='main_dishes'),
    path('bakery_productsl', views.bakery_productsl, name='bakery_productsl'),
    path('registration', views.registration, name='registration'),
    path('add_dish', views.add_dish, name='add_dish'),
    path('new_dish', views.new_dish, name='new_dish'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
