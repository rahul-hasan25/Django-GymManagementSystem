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
    return redirect('admin_plans_list')


# ADMIN Trainer
@admin_required
def admin_trainers_list(request):
    trainers = Trainer.objects.all().order_by('name')
    return render(request, 'admin_trainers_list.html', {'trainers': trainers})


@admin_required
def admin_trainer_add(request):
    if request.method == 'POST':
        name           = request.POST.get('name')
        mobile         = request.POST.get('mobile')
        specialization = request.POST.get('specialization')
        shift_timings  = request.POST.get('shift_timings')
        
        if name and mobile and specialization and shift_timings:
            Trainer.objects.create(
                name           = name,
                mobile         = mobile,
                specialization = specialization,
                shift_timings  = shift_timings,
            )
            messages.success(request, 'Trainer added successfully!')
            return redirect('admin_trainers_list')
        else:
            messages.error(request, 'Please fill in the all required fields.')
    return render(request, 'admin_trainer_form.html', {'mode':'add'})


@admin_required
def admin_trainer_edit(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    if request.method == 'POST':
        name           = request.POST.get('name')
        mobile         = request.POST.get('mobile')
        specialization = request.POST.get('specialization')
        shift_timings  = request.POST.get('shift_timings')
        
        if name and mobile and specialization and shift_timings:
            trainer.name           = name
            trainer.mobile         = mobile
            trainer.specialization = specialization
            trainer.shift_timings  = shift_timings
            trainer.save()
            
            messages.success(request, 'Trainer Updated Successfully!')
            return redirect('admin_trainers_list')
        else:
            messages.error(request, 'Please fill in the all required fields.')
    return render(request, 'admin_trainer_form.html', {'trainer':trainer, 'mode':'edit'})


@admin_required
def admin_trainer_delete(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    if request.method == 'POST':
        trainer.delete()
        messages.success(request, 'Trainer Deleted Successfully!')
        return redirect('admin_trainers_list')
    return redirect('admin_trainers_list')

# ADMIN Members
@admin_required
def admin_members_list(request):
    members = MemberProfile.objects.all().select_related('user', 'plan')
    return render(request, 'admin_members_list.html', {'members':members})


@admin_required
def admin_member_add(request):
    plans    = MembershipPlan.objects.all().order_by('duration_months')
    trainers = Trainer.objects.all().order_by('name')
    
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        full_name = request.POST.get('full_name')
        mobile    = request.POST.get('mobile')
        age       = request.POST.get('age')
        gender    = request.POST.get('gender')
        address   = request.POST.get('address')
        join_date = request.POST.get('join_date') or timezone.now().date()
        plan_id   = request.POST.get('plan_id')
        trainer_id= request.POST.get('trainer_id')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('admin_member_add')
        
        user    = User.objects.create_user(username=username, password=password, role='MEMBER')
        plan    = MembershipPlan.objects.get(id=plan_id) if plan_id else None
        trainer = Trainer.objects.get(id=trainer_id) if trainer_id else None
        
        MemberProfile.objects.create(
            user      = user,
            full_name = full_name,
            mobile    = mobile,
            age       = age,
            gender    = gender,
            address   = address,
            join_date = join_date,
            plan      = plan,
            trainer   = trainer
        )
        messages.success(request, 'Member Added Successfully!')
        return redirect('admin_members_list')
    return render(request, 'admin_member_form.html', {'plans':plans, 'trainers':trainers, 'mode':'add'})


@admin_required
def admin_member_edit(request, member_id):
    member   = MemberProfile.objects.get(id=member_id)
    plans    = MembershipPlan.objects.all().order_by('duration_months')
    trainers = Trainer.objects.all().order_by('name')
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        mobile    = request.POST.get('mobile')
        age       = request.POST.get('age')
        gender    = request.POST.get('gender')
        address   = request.POST.get('address')
        join_date = request.POST.get('join_date') or timezone.now().date()
        plan_id   = request.POST.get('plan_id')
        trainer_id= request.POST.get('trainer_id')
        
        plan    = MembershipPlan.objects.get(id=plan_id) if plan_id else None
        trainer = Trainer.objects.get(id=trainer_id) if trainer_id else None
        
        
        member.full_name = full_name
        member.mobile    = mobile
        member.age       = age
        member.gender    = gender
        member.address   = address
        member.join_date = join_date
        member.plan      = plan
        member.trainer   = trainer
        member.save()
        
        messages.success(request, 'Member Updated Successfully!')
        return redirect('admin_members_list')
    return render(request, 'admin_member_form.html', {'member':member, 'plans':plans, 'trainers':trainers, 'mode':'edit'})


@admin_required
def admin_member_delete(request, member_id):
    member = MemberProfile.objects.get(id=member_id)
    if request.method == 'POST':
        user = member.user # Get the associated user object
        member.delete()
        user.delete()
        messages.success(request, 'Member Deleted Successfully!')
        return redirect('admin_members_list')
    return redirect('admin_members_list')