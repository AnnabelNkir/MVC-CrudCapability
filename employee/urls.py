from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees_list, name='employees-list'),
    path('create/', views.create_employee, name='create-employee'),
    path('edit/<int:id>', views.edit_employee, name='edit-employee'),
]