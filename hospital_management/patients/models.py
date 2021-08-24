from django.db import models

# Create your models here.
class PatientSubmissionModel(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    ch = [('hyderabad', 'hyderabad'), ('guntur', 'guntur'), ('vijayawada', 'vijayawada')]
    location= models.CharField(max_length=20, choices=ch, default='1')
    ge = [('male', 'Male'), ('female', 'Female')]
    gender = models.CharField(max_length=20, choices=ge, default='1')
    email=models.EmailField()
    mobile=models.BigIntegerField()
    Appointment_date=models.DateField()