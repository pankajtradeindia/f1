# Generated by Django 3.2.8 on 2021-11-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(auto_now=True),
        ),
    ]
