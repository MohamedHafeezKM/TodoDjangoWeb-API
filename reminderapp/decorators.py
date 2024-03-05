from django.contrib import messages
from django.shortcuts import redirect
from reminderapp.models import Todos

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,'Invalid Session')
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper

def owner_permission_required(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get('pk')
        todo_object=Todos.objects.get(id=id)
        if todo_object.user!=request.user:
            messages.error(request,'You do not have authority')
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper