from django.shortcuts import render, redirect
from .models import RegisterModel, ApplicationModel
from .forms import RegisterForm, ApplicationForm
from django.http import HttpResponse
from django.urls import reverse


def home(request):
    return render(request, "studentapp/home.html")


def registration(request):
    if request.method == 'POST':
        regobj = RegisterForm(request.POST, request.FILES)
        if regobj.is_valid():
            regobj.save()
            return redirect('home')
    else:
        regobj = RegisterForm()
        return render(request, "studentapp/registrations.html", {"regobj": regobj})


def application(request):
    if request.method == 'POST':
        appobj = ApplicationForm(request.POST)
        if appobj.is_valid():
            appobj.save()
            return redirect('home')
    else:
        appobj = ApplicationForm()
        return render(request, "studentapp/applications.html", {"appobj": appobj})


def condidates(request):
    data = RegisterModel.objects.all()
    return render(request, "studentapp/condidatelist.html", {"data": data })


def DepartmentWise(request):
    data = RegisterModel.objects.values('department').distinct()
    return render(request, "studentapp/DepartmentList.html", {"data": data})


def SelectStudentList(request):
    data = ApplicationModel.objects.filter(marks_inter__gte=900).values()
    return render(request, "studentapp/studentlist.html", {"data": data})


def details(request, department):
    data = RegisterModel.objects.filter(department__contains=department).values()
    return render(request, "studentapp/details.html", {"data": data })
