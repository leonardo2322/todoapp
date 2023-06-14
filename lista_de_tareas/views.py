from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import CreateTasks
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #asdas
            try:
                user =User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return HttpResponse('el usuario ya existe')
        return HttpResponse('Incorrrect password')
@login_required
def Errors(request,error):
    return render(request, 'errors.html',{
        'ERROR': 'Error in the server please verify what have you done ' ,
        'desc_error': error
    })
@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def tasks(resquest):
    Tasks = Task.objects.filter(user=resquest.user, dateCompleted__isnull = True)
    return render(resquest, 'tasks.html',{'todo_Tasks': Tasks})

def signout(request):
    logout(request)
    return redirect('/')

def signin(request):
    
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form':AuthenticationForm

        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'] )
        if user is None:
             return render(request, 'signin.html',{
            'form':AuthenticationForm,
            'error':'User or password is incorrect'

            })
        else:
            login(request, user)
            return redirect('tasks')
@login_required    
def create_Task(request):

    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form': CreateTasks
        })
    else:
        try:

            form = CreateTasks(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return Errors(request)
@login_required       
def TaskDetail(request,task_id):
    print(request.user,'aqui')
    if request.method == 'GET':
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form =CreateTasks(instance=task)
            return render(request,'task_detail.html',{'task_id':task,'form':form})
        except ValueError:
            return Errors(request,'error')
    else:
        try:

            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = CreateTasks(request.POST,instance=task)
            form.save()
            return redirect('tasks')
        except:

            return Errors(request,'error 404')
@login_required       
def complete(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
        
    if request.method == 'POST':
            task.dateCompleted = timezone.now()
            task.save()
            return redirect('tasks')
@login_required 
def delete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user= request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
@login_required
def completed_task(request):
    task = Task.objects.filter(user=request.user, dateCompleted__isnull = False).order_by('-dateCompleted')
    return render(request,'tasks.html', {'todo_Tasks':task})