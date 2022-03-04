from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=200, null=True)
    emp_email = models.EmailField(max_length=50,null=True)
    emp_contact = models.CharField(max_length=20, null=True)
    emp_role = models.CharField(max_length=200, null=True)
    emp_salary = models.IntegerField(null=True)

    def __str__(self):
        return self.emp_name

    def create_employee(self):
        self.save()

    def delete_employee(self):
        self.delete()
        
    def edit_employee(self):
        self.edit()