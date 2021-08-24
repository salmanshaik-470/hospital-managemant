from datetime import datetime, timedelta

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView, UpdateView, DeleteView
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


def setcookie(request):
    reponse = HttpResponseRedirect('main')
    reponse.set_signed_cookie('ip', IPAddr, salt='ip', expires=datetime.utcnow() + timedelta(days=2))
    return reponse


class Base(TemplateView):
    template_name = 'base.html'


# Create your views here.
class Main(View):
    def post(self, request):
        fm = PatientSubmissionForm(request.POST)
        if fm.is_valid():
            fm.Appointment_date = request.POST.get('date')
            fm.save(commit=True)
        return HttpResponse('Appointment is sucessfully booked')

    def get(self, request):
        fm = PatientSubmissionForm()
        self.request.session['time'] = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        return render(request, 'main.html',
                      {'form': fm, 'ip': self.request.get_signed_cookie('ip', default='Not Detected', salt='ip'),
                       'time': self.request.session['time']})
