# Generated by Django 3.2.9 on 2022-03-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200, null=True)),
                ('emp_email', models.EmailField(max_length=50, null=True)),
                ('emp_contact', models.CharField(max_length=20, null=True)),
                ('emp_role', models.CharField(max_length=200, null=True)),
                ('emp_salary', models.IntegerField(null=True)),
            ],
        ),
    ]
