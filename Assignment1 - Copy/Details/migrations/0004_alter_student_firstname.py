# Generated by Django 4.1 on 2022-08-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0003_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=25),
        ),
    ]
