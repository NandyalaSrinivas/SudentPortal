from django import forms
from .models import Register, Application


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = "__all__"


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = ["name", "email", "marks_ssc", "marks_inter"]
