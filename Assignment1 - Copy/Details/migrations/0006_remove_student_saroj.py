# Generated by Django 4.1 on 2022-08-25 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0005_student_saroj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='saroj',
        ),
    ]