from django.shortcuts import render,redirect

import employee
from .models import Employee
from .forms import *
from .forms import EmployeeForm

def employees_list(request):
    employees = Employee.objects.order_by('-id')
    context = {
        'employees': employees,
    }
    return render(request, 'list.html', context)

def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    form = EditEmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EditEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'edit.html', context)

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'delete.html', context)