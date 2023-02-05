from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mensaje (req):
    return HttpResponse("calculadora")
def f_suma(num1,num2):
    result = int(num1) + int(num2)
    return result
def f_resta(num1,num2):
    result = int(num1) - int(num2)
    return result
def f_multiplicacion(num1,num2):
    result = int(num1) * int(num2)
    return result
def f_divicion(num1,num2):
    if num2=="0":
        result="error divición entre 0"
    else:
        result = int(num1) / int(num2)
    return result
    
def home(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'suma' in request.POST:
            result = f_suma(num1,num2)
            return render(request,'index.html',{'result':result})
        if 'resta' in request.POST:
            result = f_resta(num1,num2)
            return render(request,'index.html',{'result':result})
        if 'multiplicacion' in request.POST:
            result =f_multiplicacion(num1,num2)
            return render(request,'index.html',{'result':result})
        if 'divicion' in request.POST:
            result = f_divicion(num1,num2)
            return render(request,'index.html',{'result':result})
    return render(request,'index.html')