from django.urls import path,include
from . import views
# viewsets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employeeData',views.EmployeeViewModelSet,basename="task")



urlpatterns = [
#     path('task/',views.taskView,name='taskView'),
#     path('tasks/<int:pk>/',views.taskObjectView),
# class based view
#     path('tasks/',views.StudentObjectViewCode.as_view(),name='task'),
#     path('task/<int:pk>/',views.StudentObjectUpdateView.as_view(),name='taskView'),

# mixins
#     path('employee/',views. EmployeeGetAll.as_view()),
#     path('employee/<int:pk>/',views.EmployeeGetIdDetails.as_view()),

# generics
#       path('Employee/',views.EmployeeListView.as_view()),
#       path('Employee/<int:pk>/',views.EmployeeUpdateObject.as_view()),


# viewsets
    path('',include(router.urls)),
 ]
