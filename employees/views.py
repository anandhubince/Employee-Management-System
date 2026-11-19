from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

import employees
from .models import Employee
@login_required
def add_employee(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        department=request.POST.get('department')
        salary=request.POST.get('salary')
        joining_date=request.POST.get('joining_date')
        Employee.objects.create(
            name=name,
            age=age,
            email=email,
            phone=phone,
            department=department,
            salary=salary,
            joining_date=joining_date
        )
        return redirect('view_employees')
    return render(request,'add_employee.html')

@login_required
def view_employees(request):
    employees=Employee.objects.all()
    return render(request,'view_employees.html',{'employees':employees})

@login_required
def edit_employee(request,id):
    employees=Employee.objects.get(id=id)
    if request.method=='POST':
        employees.name=request.POST.get('name') or employees.name
        employees.age=request.POST.get('age') or employees.age
        employees.email=request.POST.get('email') or employees.email
        employees.phone=request.POST.get('phone') or employees.phone
        employees.department=request.POST.get('department') or employees.department
        employees.salary=request.POST.get('salary') or employees.salary
        employees.joining_date=request.POST.get('joining_date') or employees.joining_date
        employees.save()
        return redirect('view_employees')
    return render(request, 'edit_employees.html', {'employees':employees})

@login_required
def delete_employee(request, id):
    view_employees = Employee.objects.get(id=id)
    if request.method == 'POST':
        view_employees.delete()
        return redirect('view_employees')
    return render(request, 'delete_employee.html', {'employees': employees})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check whether username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists. Please choose another username.'
            })
        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect('login')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_employees')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
