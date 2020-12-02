from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    marks_ssc = models.CharField(max_length=3)
    marks_inter = models.CharField(max_length=3)
    is_selected = models.BooleanField(default=True)


class Register(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
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
    pic = models.ImageField(blank= True, upload_to='images/')


