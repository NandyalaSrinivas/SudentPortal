from django.db import models


class Application(models.Model):
    registers = models.OneToOneField(RegisterModel, on_delete=models.CASCADE)
    marks_ssc = models.CharField(max_length=3)
    marks_inter = models.CharField(max_length=3)


class Register(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    DEPART_CHOICES = [
        ('CSE', 'CS'),
        ('IT', 'IT'),
        ('ECE', 'EC'),
        ('EEE', 'EE'),
        ('CIVIL', 'CVL'),
        ('MECH', 'ME'),
    ]
    department = models.CharField(max_length=10, choices=DEPART_CHOICES)
    nationality = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    pic = models.ImageField(upload_to='images/')


