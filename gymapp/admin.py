from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role', )}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    list_filter  = ['role', 'is_staff', 'is_superuser', 'is_active']
    
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display  = ['name', 'duration_months', 'fee']
    search_fields = ['name', 'duration_months']
    list_filter   = ['name', 'duration_months']

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'specialization', 'shift_timings']
    search_fields = ['name', 'shift_timings']
    
class MemberProfileAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'user', 'mobile', 'plan', 'join_date']
    search_fields = ['full_name', 'user__username', 'mobile']
    list_filter   = ['plan', 'join_date']

class EquipmentAdmin(admin.ModelAdmin):
    list_display  = ['name', 'units', 'price', 'purchase_date', 'is_active']
    search_fields = ['name', 'price']

class PaymentAdmin(admin.ModelAdmin):
    list_display  = ('member', 'plan', 'amount', 'payment_date', 'mode', 'status')
    list_filter   = ('status', 'mode', 'payment_date')
    search_fields = ('member__full_name', 'plan__name')
    
class AttendanceAdmin(admin.ModelAdmin):
    list_display  = ('member', 'date', 'time_in', 'attendance_status')
    list_filter   = ('date',)
    search_fields = ('member__full_name',)
    
    def attendance_status(self, obj):
        if obj.time_in:
            return "Present"
        return "Absent"

    attendance_status.short_description = "Status"

class EnquiryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'mobile', 'status', 'created_at']
    search_fields = ['name', 'email', 'mobile']
    list_filter   = ['status', 'created_at']

class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display  = ('title', 'member', 'short_description', 'created_at')
    list_filter   = ('created_at',)
    search_fields = ('title', 'member__full_name')
    
    def short_description(self, obj):
        if obj.description and len(obj.description) > 40:
            return obj.description[:40] + "..."
        return obj.description

    short_description.short_description = "Description Preview"

class FeedbackAdmin(admin.ModelAdmin):
    list_display  = ('member', 'short_message', 'created_at')
    list_filter   = ('created_at',)
    search_fields = ('member__full_name', 'message')
    
    def short_message(self, obj):
        if obj.message and len(obj.message) > 50:
            return obj.message[:50] + "..."
        return obj.message

    short_message.short_description = "Message Preview"

admin.site.register(User, UserAdmin)
admin.site.register(MembershipPlan, MembershipPlanAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(MemberProfile, MemberProfileAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(Feedback, FeedbackAdmin)