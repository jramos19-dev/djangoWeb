from django.shortcuts import render
from django import forms

# Create your views here.
tasks=["foo", "var","baz"]

class newTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.NumberInput()

def index(request):
    return render(request, "tasks/index.html",{
        "tasks" :tasks
    })

def add(request):
    return render(request, "tasks/add.html",{
       
        "form" : newTaskForm()
    })