from django.shortcuts import render

def main(request):
    return render(request, 'main.html')


def apply(request):
    return render(request,'apply.html')


def gameresult(request):
    return render(request, 'gameresult.html')

def mystatus(request):
    return render(request, 'mystatus.html')
# Create your views here.
