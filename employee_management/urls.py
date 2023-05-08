"""employee_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin_logout/", views.admin_logout, name="admin_logout"),
    path("admin_change_password/", views.admin_change_password, name="admin_change_password"),
    path("admin_all_employees/", views.admin_all_employees, name="admin_all_employees"),
    path('',views.index_page,name='index'),
    path('registration/',views.registration_page,name='registration'),
    path("emp_login/", views.emp_login, name="emp_login"),
    path('emp_logout/',views.emp_logout,name='emp_logout'),
    path('home_page/', views.home_page,name='home_page'),
    path('emp_profile/', views.emp_profile,name='emp_profile'),
    path('emp_exp/', views.emp_experience,name='emp_exp'),
    path('edit_exp/', views.edit_experience,name='edit_exp'),
    path('emp_education/', views.emp_education,name='emp_education'),
    path('edit_education/', views.edit_education,name='edit_education'),
    path('change_password/', views.change_password,name='change_password'),
]