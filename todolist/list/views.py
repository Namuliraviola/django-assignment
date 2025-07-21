from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm  # will create this next

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'list/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'list/add_task.html', {'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
         task = form.save(commit=False)  
         task.user = request.user        
         task.save() 
        return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'list/update_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
