from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})



"""
def operation(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res1 = x+y
    res2 = x-y
    res3 = x*y
    res4 = x/y
    return render(request,"result.html",{'Addition':res1, 'Subtraction':res2, 'Multiplication':res3, 'Division':res4})"""