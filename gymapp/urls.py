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
    #ADMIN Attendance
    path('admin_attendaces/', views.admin_attendance_list, name='admin_attendance_list'),
    path('admin_attendance_add/', views.admin_attendance_add, name='admin_attendance_add'),
    #ADMIN Equipment
    path('admin_equipments/', views.admin_equipment_list, name='admin_equipment_list'),
    path('admin_equipment_add/', views.admin_equipment_add, name='admin_equipment_add'),
    path('admin_equipment_edit/<int:equipment_id>/', views.admin_equipment_edit, name='admin_equipment_edit'),
    path('admin_equipment_delete/<int:equipment_id>/', views.admin_equipment_delete, name='admin_equipment_delete'),
    #ADMIN Enquiry
    path('admin_enquiries_list/', views.admin_enquiries_list, name='admin_enquiries_list'),
    path('admin_enquiries_list_update/<int:enquiry_id>/', views.admin_enquiry_update_status, name='admin_enquiry_update_status'),
    #ADMIN Workout Plan
    path('admin_workout_plans/', views.admin_workout_plans_list, name='admin_workout_plans_list'),
    path('admin_workout_plan_add/', views.admin_workout_plan_add, name='admin_workout_plan_add'),
    path('admin_workout_plan_delete/<int:plan_id>/', views.admin_workout_plan_delete, name='admin_workout_plan_delete'),
]