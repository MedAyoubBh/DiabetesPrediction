from django.shortcuts import render


def home(request):
    return render(request,"home.html")

def predict(request):
    return render(request,"predict.html")

def result(request):
    
    return render(request,"negative.html")