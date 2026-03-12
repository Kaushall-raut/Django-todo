from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.urls import reverse
# Create your views here.

def task_list(request):
    task =Task.objects.all().order_by('-created_at')
    return render(request,'todo/task_list.html',{'task':task})

def add_task(request):
    if request.method == 'POST':
        title=request.POST.get('title').strip()
        description=request.POST.get('description').strip()
        if title:
            Task.objects.create(title=title,description=description)
            return redirect(reverse("todo:task_list"))
        else :
            error="Title cannot be empty"
            return render(request,'todo/task_form.html',{'error':error})

        
    return render(request,'todo/task_form.html')


def update_task(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        title=request.POST.get('title').strip()
        description=request.POST.get('description').strip()
        completed=request.POST.get('completed')== 'on'

        if title:
            task.title=title
            task.description=description
            task.completed=completed
            task.save()
            return redirect(reverse("todo:task_list.html"))
        
def delete_task(request,id):

    task=get_object_or_404(Task,id=id)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))

    return render(request,'todo/delete.html',{'task':task})