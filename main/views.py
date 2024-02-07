from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
from django.db import models
from .models import Task
from .forms import TaskForm
from django.views.generic import UpdateView,DetailView,DeleteView

# index view
def index(request):
    tasks  = Task.objects.order_by('id')
    return render(request,'main/index.html',{'title':'Home page',
                                            'tasks':tasks })



# Task detail view
class TaskDetailsView(DetailView):
    model = Task
    template_name='main/detail_task.html'
    context_object_name='task'

# Task Update view
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/edit.html'

    form_class=TaskForm
    success_url='/home/'

# Task delete view
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'main/delete.html'
    success_url='/home/'

# About view
def about(request):
    return render(request,'main/about.html')

    

# create view
def create(request):
    error=''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Error form'

    form = TaskForm()
    context = {
        'form': form,
        'error':error
    }
    return render(request,'main/create.html', context)