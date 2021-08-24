from django import forms
from .models import *


class PatientSubmissionForm(forms.ModelForm):
        class Meta:
            model = PatientSubmissionModel
            fields = '__all__'
            widgets = {
                'Appointment_date' : forms.SelectDateWidget()
            }