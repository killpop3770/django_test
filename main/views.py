from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all().order_by('-id')  # [:0]
    return render(request, "main/index.html", {'title': 'CMS', 'tasks': tasks})
    # return HttpResponse("<h4>Hello, world!</h4>")


def about(request):
    return render(request, "main/about.html")


def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Ошибка в данных форм!"
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/create.html", context)
