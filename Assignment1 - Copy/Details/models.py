from django.db import models
import datetime as dt

# Create your models here.


class Student(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=255)
    dob=models.DateField()
    roll_number=models.IntegerField()
    department_name=models.CharField(max_length=255)
    course_name=models.CharField(max_length=255)
    semester_number=models.IntegerField()

    @property
    def age_calc(self):
        current_date= dt.datetime.today()
        temp=str(self.dob)
        dob_year=dt.datetime.strptime(temp,"%Y-%m-%d").date().year
        age=current_date.year - dob_year
        return age


class Department(models.Model):
    department_name=models.CharField(max_length=255)
    # department_name=models.ForeignKey(Student.department_name,on_delete=models.CASCADE)
    course_number=models.IntegerField()
    teacher_number=models.IntegerField()


