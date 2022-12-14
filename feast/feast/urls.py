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
    path('first_meal', views.first_meal, name='first_meal'),
    path('main_dishes', views.main_dishes, name='main_dishes'),
    path('bakery_productsl', views.bakery_productsl, name='bakery_productsl'),
    path('salads', views.salads, name='salads'),
    path('beverages', views.beverages, name='beverages'),
    path('registration', views.registration, name='registration'),
    path('my_recipes', views.my_recipes, name='my_recipes'),
    path('add_dish', views.add_dish, name='add_dish'),
    path('new_dish', views.new_dish, name='new_dish'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dish_info/<int:id>', views.dish_info, name='dish_info'),
    path('edit_dish/<int:id>', views.edit_dish, name='edit_dish'),
    path('save_edit_dish/<int:id>', views.save_edit_dish, name='save_edit_dish'),
    path('delete_dish/<int:id>', views.delete_dish, name='delete_dish'),
    path('export', views.export, name='export'),
]
