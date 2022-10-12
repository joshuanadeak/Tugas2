# For some of the def functions, credits to Rendy Arya Kemal for the inspirations
# Register, Login, Logout is Using The Template Given From The Lab

from django.forms import ModelForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from todolist.models import Task
from django import forms
from django.http.response import HttpResponse
from django.core import serializers

# Isi Views
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user).order_by('date')
    context = {
        'list_todolist': data_todolist,
        'nama': 'Joshua Mihai Daniel Nadeak',
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Has Been Successfully Created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            return redirect("todolist:show_todolist")
        else:
            messages.info(request, 'Your Username or Password is Wrong!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url="/todolist/login")
def logout_user(request):
    logout(request)
    return redirect("todolist:login")

@login_required(login_url='/todolist/login/')
def create_todolist(request):
    form = NewForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            date = form.cleaned_data["date"]
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            user = request.user
            task = Task(date = date, title = title, description = description, user = user)
            task.save()
            messages.success(request, "Your Task Has Been Saved!")
            return redirect("todolist:show_todolist")
    form = NewForm();
    context = {"form": form}
    return render(request, "create_task.html", context)

@login_required(login_url='/todolist/login/')
def delete_todolist(request, id):
    task = Task.objects.get(pk = id, user = request.user)
    if task:
        task.delete()
        messages.success(request, "Deleted Successfully!")
    else:
        messages.error(request, "An Error Has Occurred While Deleting!")
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def update_todolist(request, id):
    task = Task.objects.get(pk = id, user = request.user)
    if task:
        task.is_finished = not task.is_finished
        task.save()
        messages.success(request, "Updated Successfully!")
    else:
        messages.error(request, "An Error Has Occurred While Updating!")
    return redirect("todolist:show_todolist")

class NewForm(forms.Form):
    date = forms.DateField(label = "Date")
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={"cols": ""}))

@login_required(login_url="/todolist/login")
def get_todo_json(request):
    todos = Task.objects.filter(user=request.user).order_by("data").all()
    return HttpResponse(
        serializers.serialize("json", todos), content_type="application/json"
    )

@login_required(login_url="/todolist/login")
def add_todo_json(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            task = Task(
                date=request.POST["date"],
                title=request.POST["title"],
                description=request.POST["description"],
                user=request.user,
            )
            task.save()
            return HttpResponse(
                serializers.serialize("json", [task]),
                content_type="application/json",
            )
    return HttpResponse("Invalid method", status_code=405)