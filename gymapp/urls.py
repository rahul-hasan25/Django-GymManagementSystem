from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin-login/', views.admin_login_view, name='admin_login_view'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout_view'),
    # ADMIN Plan
    path('admin_plans_list/', views.admin_plans_list, name='admin_plans_list'),
    path('admin_plan_add/', views.admin_plan_add, name='admin_plan_add'),
    path('admin_plans_edit/<int:plan_id>/', views.admin_plan_edit, name='admin_plan_edit'),
    path('admin_plans_delete/<int:plan_id>/', views.admin_plan_delete, name='admin_plan_delete'),
    # ADMIN Trainer
    path('admin_trainers/', views.admin_trainers_list, name='admin_trainers_list'),
    path('admin_trainers_add/', views.admin_trainer_add, name='admin_trainer_add'),
    path('admin_trainers_edit/<int:trainer_id>/', views.admin_trainer_edit, name='admin_trainer_edit'),
    path('admin_trainer_delete/<int:trainer_id>/', views.admin_trainer_delete, name='admin_trainer_delete'),
    # ADMIN Members
    path('admin_members/', views.admin_members_list, name='admin_members_list'),
    path('admin_member_add/', views.admin_member_add, name='admin_member_add'),
    path('admin_member_edit/<int:member_id>/', views.admin_member_edit, name='admin_member_edit'),
    path('admin_member_delete/<int:member_id>/', views.admin_member_delete, name='admin_member_delete'),
]