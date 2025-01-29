from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to task management system")

def contact(request):
    return HttpResponse("<h1 style='color:red;'>This is contact page.</h1>")
def show_task(request):
    return HttpResponse("This your task.")
def show_specific_task(request,id):
    print("Your id is = ")
    print("id",id)
    print("id type",type(id))
    return HttpResponse("This is your Specific task")

