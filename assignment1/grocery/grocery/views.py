from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"home.html")

def payments(request):
    return render(request,"payment.html")

def staff(request):
    return render(request,"staff.html")

def customer(request):
    return render(request,"customer.html")

def product(request):
    return render(request,"products.html")





