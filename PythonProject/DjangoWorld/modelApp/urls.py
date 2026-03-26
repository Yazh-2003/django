from django.urls import path
from . import views

urlpatterns = [
    path('tracker/',views.DailyTracker,name='tracker'),
    path('registerHere/',views.RegisterForm,name='register'),
]