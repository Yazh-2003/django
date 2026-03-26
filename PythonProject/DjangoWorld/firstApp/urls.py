from django.urls import path,include
from . import views

urlpatterns = [
    path('Home/',views.Welcome,name='home'),
    path('template/',views.templateView,name='template'),
    path('studentInfo/',views.StudentInfo,name='student'),
    path('studentdetail/',views.studentDetails,name='detail'),
    path('home/<str:name>/<int:age>/',views.home,name='home'),
    path('indexpage/<str:name>/<int:age>/',views.indexPage,name='indexpage'),
    path('template_1/',views.myTemplate,name='template'),
    path('homepage/',views.homePage,name='homepage'),
    path('bird/',views.bird_Detail,name='bird_detail'),
]