from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(request,"newyear/index.html")



def home(request):
    return render(request,"pdf_app/home.html")


