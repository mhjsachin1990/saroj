from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student,Department

# Create your views here.


"""       >>>>>> ***** STUDENTS ******* <<<<<<     """


def home(request):
    return render(request,'home.html')


def students(request):
    students = Student.objects.all().values()
    template=loader.get_template('students.html')
    context={
        'students':students,
    }

    return HttpResponse(template.render(context,request))


def add_students(request):
    template=loader.get_template('add_students.html')
    return HttpResponse(template.render({},request))


def addrecord(request):
    a = request.POST['firstname']
    b = request.POST['lastname']
    c = request.POST['dob']
    d = request.POST['roll_number']
    e = request.POST['department_name']
    f = request.POST['course_name']
    g = request.POST['semester_number']
    students=Student(firstname=a,lastname=b,dob=c,roll_number=d,department_name=e,course_name=f,semester_number=g)
    students.save()
    return HttpResponseRedirect(reverse('students'))


def delete(request,id):
    students=Student.objects.get(id=id)
    students.delete()
    return HttpResponseRedirect(reverse('students'))


def update(request,id):
    students=Student.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'students':students,
    }
    return HttpResponse(template.render(context,request))


def updaterecord(request,id):
    a = request.POST['firstname']
    b = request.POST['lastname']
    c = request.POST['dob']
    d = request.POST['roll_number']
    e = request.POST['department_name']
    f = request.POST['course_name']
    g = request.POST['semester_number']
    students = Student.objects.get(id=id)
    students.firstname=a
    students.lastname=b
    students.dob=c
    students.roll_number=d
    students.department_name=e
    students.course_name=f
    students.semester_number=g
    students.save()
    return HttpResponseRedirect(reverse('students'))


"""       >>>>>> ***** DEPARTMENT ******* <<<<<<     """


def department(request):
    dept=Department.objects.all().values()
    template=loader.get_template('department.html')
    context={
        'department':dept,
    }
    return HttpResponse(template.render(context,request))


def add_dept(request):
    template = loader.get_template('add_dept.html')
    return HttpResponse(template.render({}, request))


def add_department(request):
    a = request.POST['department_name']
    b = request.POST['course_number']
    c = request.POST['teacher_number']
    dept=Department(department_name=a,course_number=b,teacher_number=c)
    dept.save()
    return HttpResponseRedirect(reverse('department'))


def delete_dept(request,id):
    dept = Department.objects.get(id=id)
    dept.delete()
    return HttpResponseRedirect(reverse('department'))


def update_dept(request,id):
    dept=Department.objects.get(id=id)
    template=loader.get_template('update_dept.html')
    context={
        'department':dept,
    }
    return HttpResponse(template.render(context,request))


def update_department(request,id):
    a = request.POST['department_name']
    b = request.POST['course_number']
    c = request.POST['teacher_number']
    dept=Department.objects.get(id=id)
    dept.department_name=a
    dept.course_number=b
    dept.teacher_number=c
    dept.save()
    return HttpResponseRedirect(reverse('department'))

