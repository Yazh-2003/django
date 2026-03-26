from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.registerForm,),
    path('response/',views.responseForm,),
    path('sample/',views.sampleFormTemplate,name='sampleForm'),

]