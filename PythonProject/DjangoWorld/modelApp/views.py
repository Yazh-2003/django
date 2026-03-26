from django.shortcuts import render,redirect
from .models import DailyExpenseTracker
from .forms import dailyForm
from django.http import HttpResponse



# Create your views here.
def DailyTracker(request):
    expenses = DailyExpenseTracker.objects.all()
    return render(request,'tracker/expensetracker.html',{'expenses':expenses})

def RegisterForm(request):
    if request.method == 'POST':
        form = dailyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tracker")
        return HttpResponse("<p>Invalid credentials</p>")
    form = dailyForm
    return render(request,'tracker/registerModel.html',{'form':form})
