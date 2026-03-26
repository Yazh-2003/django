from django.shortcuts import render


# Create your views here.
def homePage(request):
    return render(request,'thirdApp/homePage.html')


def contact(request):
    info={'name':'yaazh',
          'email':'yaazhini@gmail.com'}
    return render(request,'thirdApp/contact.html',{'info':info})