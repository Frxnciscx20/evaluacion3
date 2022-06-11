from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def feriados(request):
    return render(request, 'feriados.html')
    
def formContacto(request):
    return render(request,'formContacto.html')

def formReg(request):
    return render(request,'formReg.html')

def fotos(request):
    return render(request,'fotos.html')

def productos(request):
    return render(request,'productos.html')

def qsomos(request):
    return render(request,'qsomos.html')
