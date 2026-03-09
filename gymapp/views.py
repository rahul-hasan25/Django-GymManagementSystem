from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        mobile  = request.POST.get('mobile')
        message = request.POST.get('email')
        
        if name and email and mobile and message:
            Enquiry.objects.create(name=name, email=email, mobile=mobile, message=message)
            messages.success(request, 'Your enquiry has been submitted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in the all fields.')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and getattr(user, 'role', None) == 'ADMIN':
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credential or not an admin')
            return redirect('admin_login_view')
    return render(request, 'admin_login.html')


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or getattr(request.user, 'role', None) != 'ADMIN':
            messages.error(request, 'You must be an Admin to access this page.')
            return redirect('admin_login_view')
        return view_func(request, *args, **kwargs)
    return wrapper

@admin_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('home')


@admin_required
def admin_plans_list(request):
    plans = MembershipPlan.objects.all().order_by('duration_months')
    return render(request, 'admin_plans_list.html', {'plans':plans})


@admin_required
def admin_plan_add(request):
    if request.method == 'POST':
        name            = request.POST.get('name')
        duration_months = request.POST.get('duration_months')
        fee             = request.POST.get('fee')
        description     = request.POST.get('description')
        
        if name and duration_months and fee:
            MembershipPlan.objects.create(
                name=name,
                duration_months=duration_months,
                fee=fee,
                description=description,
            )
            messages.success(request, 'Membership Plan added successfully!')
            return redirect('admin_plans_list')
        else:
            messages.error(request, 'Please Fill in all required fields.')
    return render(request, 'admin_plan_form.html', {'mode':'add'})


@admin_required
def admin_plan_edit(request, plan_id):
    plan = MembershipPlan.objects.get(id=plan_id)
    if request.method == 'POST':
        name            = request.POST.get('name')
        duration_months = request.POST.get('duration_months')
        fee             = request.POST.get('fee')
        description     = request.POST.get('description')
        
        if name and fee and duration_months:
            plan.name            = name
            plan.duration_months = duration_months
            plan.fee             = fee
            plan.description     = description
            plan.save()
            
            messages.success(request, 'Membership Plan Updated Successfully!')
            return redirect('admin_plans_list')
        else:
            messages.error(request, 'Please Fill in all required fields.')
    return render(request, 'admin_plan_form.html', {'plan': plan, 'mode':'edit'})


@admin_required
def admin_plan_delete(request, plan_id):
    plan = MembershipPlan.objects.get(id=plan_id)
    if request.method == 'POST':
        plan.delete()
        messages.success(request, 'Membership Plan Deleted Successfully.')
        return redirect('admin_plans_list')
    return redirect('admin_plans_list.html')