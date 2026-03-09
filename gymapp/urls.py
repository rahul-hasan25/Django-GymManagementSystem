from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin-login/', views.admin_login_view, name='admin_login_view'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout_view'),
    path('admin_plans_list/', views.admin_plans_list, name='admin_plans_list'),
    path('admin_plan_add/', views.admin_plan_add, name='admin_plan_add'),
    path('admin_plans_edit/<int:plan_id>/', views.admin_plan_edit, name='admin_plan_edit'),
    path('admin_plans_delete/<int:plan_id>/', views.admin_plan_delete, name='admin_plan_delete'),
]