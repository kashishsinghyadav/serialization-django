from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

# #for only single instance
def stu_det(request,pk):
    stu=Student.objects.get(id=pk)
    
    serial=StudentSerializer(stu)
    return JsonResponse(serial.data)

    # print(serial)
    # print(serial.data)
    # jsondata=JSONRenderer().render(serial.data)
    # print(jsondata)
    # return HttpResponse(jsondata,content_type='application/json')




#for query set
def stu_list(request):
    stu=Student.objects.all()
    
    serial=StudentSerializer(stu,many=True)
   
    jsondata=JSONRenderer().render(serial.data)
    # return JsonResponse(serial.data,safe=false)
    
    return HttpResponse(jsondata,content_type='application/json')

