from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *
from .models import *
from patients.models import PatientSubmissionModel
from patients.forms import PatientSubmissionForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash

# Create your views here.



class SignUpView(View):
    def post(self,request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'account created')
                form.save()
                return HttpResponseRedirect('login')
            return render(request, 'signup.html', {'form': form})
    def get(self,request):
        form = SignUpForm()
        return render(request,'signup.html',{'form':form})

def user_login(request):
    # if not request.user.is_authenticated:
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('appt')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})



class Appointment(View):
    def get(self,request):
        print(request.method)
        app=PatientSubmissionModel.objects.all()
        return render(request,'appoinment.html',{'app':app})


class update(View):
    def post(self,request,id):
        data = PatientSubmissionModel.objects.get(pk=id)
        fm = PatientSubmissionForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            messages.info(request, "You have updated Successfully!!")
            return HttpResponseRedirect("/email")
    def get(self,request,id):
       data = PatientSubmissionModel.objects.get(pk=id)
       fm = PatientSubmissionForm(instance=data)
       return render(request, 'conform.html', {'fm': fm})
def DisplayEmail(request):
    if request.method == 'POST':
        to =  request.POST.get('email')
        content = request.POST.get('first_name')+' Your Appointment Confirmed'+'/n it is  auto generated mail please do not replay'
        print(to,content)
        send_mail(
            "Appointment",
            content,
            settings.EMAIL_HOST_USER,
            [to]
        )
        return HttpResponse('<h1>Appointment successfully registered</h1>')
    else:
        return redirect('/')

def log_out(request):
  logout(request)
  return HttpResponseRedirect('/')