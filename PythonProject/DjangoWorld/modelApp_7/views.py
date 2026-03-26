from django.shortcuts import render
from .models import TaskAndDeadlinePlanner
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from employeeApp .models import EmployeeModel
from employeeApp .serializers import EmployeeSerializer
from rest_framework import viewsets
# mixins
from rest_framework import mixins
from rest_framework import generics
# Create your views here.
# def taskView(request):
#     task = TaskAndDeadlinePlanner.objects.all()
#     task_list = list(task.values())
#     return JsonResponse(task_list, safe=False)
@api_view(['GET','POST'])
def taskView(request):
    if request.method == 'GET':
       tasks = TaskAndDeadlinePlanner.objects.all()
       serializer = TaskSerializer(tasks, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        tasks= TaskSerializer(data=request.data)
        if tasks.is_valid():
            tasks.save()
            return Response(tasks.data, status=status.HTTP_201_CREATED)
        return Response(tasks.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
def taskObjectView(request,pk):
    try:
        task= TaskAndDeadlinePlanner.objects.get(pk=pk)
    except TaskAndDeadlinePlanner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StudentObjectViewCode(APIView):
    def get(self,request):
        task=TaskAndDeadlinePlanner.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentObjectUpdateView(APIView):
    def get_object(self,pk):
        try:
            return TaskAndDeadlinePlanner.objects.get(pk=pk)
        except TaskAndDeadlinePlanner.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        task=self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def put(self, request,pk):
        student=self.get_object(pk)
        serializer = TaskSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        task=self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# MIXINS

class EmployeeGetAll(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


    def get(self,request):
        return self.list(request)
    # create new data
    def post(self,request):
        return self.create(request)

# get a single data with <id>

class EmployeeGetIdDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    # get a single data
    def get(self,request,pk):
        return self.retrieve(request,pk)
    # update data
    def put(self,request,pk):
        return self.update(request,pk)
    # delete data
    def delete(self,request,pk):
        return self.destroy(request,pk)


# Generics
class EmployeeListView(generics.ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateObject(generics.RetrieveUpdateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


# Viewsets
class EmployeeViewModelSet(viewsets.ViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    def list(self,request):
        employee = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return (serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        employee =EmployeeModel.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def update(self,request,pk):
        employee = EmployeeModel.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employee = EmployeeModel.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
