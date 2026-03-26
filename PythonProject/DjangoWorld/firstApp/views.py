from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def Welcome(request):
    return HttpResponse("Welcome to World")

def templateView(request):
    return HttpResponse("<h1>Django Learning </h1>")

def StudentInfo(request):
    studentName="Yaazh"
    return HttpResponse(studentName)

def studentDetails(request):
    studentName="""
    <html>
       <head>
           <title>Django Learning </title>
       </head>
           <body>
               <h1>Yaazh</h1>
               <h1>Female</h1>
               <h1>B.Tech</h1>
               <h1>Python fullstack</h1>
           </body>
    </html>"""
    return HttpResponse(studentName)

def home(request,name,age):
    return HttpResponse(f" i am {name} and {age}")

def indexPage(request,name,age):
    return redirect("home",name=name,age=age)

def myTemplate(request):
    return render(request,"App/home.html")


def homePage(request):
    return render(request,"App/homePage.html",context={"name":"Yaazh","age":22})


def bird_Detail(request):
    bird_data={
        'name' : 'Flamingo',
        'biological_name' : 'Phoenicopterus',
        'habitat' : 'Lakes, lagoons, and wetlands',
        'food' : 'Algae, small shrimp, and crustaceans',
        'color' : 'pink',
        'lifespan' : '20-30 years',
        'image' : 'flamingo1.jpg'
    }
    return render(request,"App/bird.html",{"bird":bird_data})

