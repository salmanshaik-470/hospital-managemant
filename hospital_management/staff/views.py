from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def staff(request):
    return render(request,'staff.html')
