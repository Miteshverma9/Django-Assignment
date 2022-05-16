from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"home.html")

def customer_page(request):
    return render(request,"customer.html")

def staff_page(request):
    return render(request,"staff.html")

def vehicle_page(request):
    return render(request,"vehicle.html")




