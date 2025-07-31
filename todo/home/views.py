from django.shortcuts import render, get_object_or_404,redirect
from home.models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(name = task )
        return redirect('home')

    tasks_list = Task.objects.all().order_by('complete', '-important')

    return render(request, 'index.html', context={'tasks':tasks_list})

def update_task(request, task_id):
    task = Task.objects.get(id = task_id)
    # task = get_object_or_404(Task, id=task_id) 

    if request.method == 'POST':
        if 'important' in request.POST:
            task.important = not task.important
            task.save()
        else:
            task.complete = not task.complete
            task.save()

        
        
    
    return redirect('home')

# def important_task(request, task_id):
#     if request.method == 'POST':
#         task = get_object_or_404(Task, id=task_id)
#         task.important = not task.important
#         task.save()
#     return redirect('home')

def del_task(request, task_id):  
    Task.objects.get(id=task_id).delete()    
    return redirect('home')





    


    
