from django.shortcuts import render
from .forms import sampleForm
# Create your views here.
def registerForm(request):
    return render(request,'formApp/register.html')

def responseForm(request):
    UserName=request.GET.get('username')
    Password=request.GET.get('password')
    Email=request.GET.get('email')
    PhoneNo=request.GET.get('phoneNo')

    DateOfBirth=request.GET.get('dateOfBirth')
    return render(request,'formApp/response.html',{'username':UserName,'password':Password,'email':Email,
                                                   'phoneNo':PhoneNo,'dateOfBirth':DateOfBirth})


def sampleFormTemplate(request):
    form= sampleForm
    return render(request,'formApp/form.html',{'form':form})
