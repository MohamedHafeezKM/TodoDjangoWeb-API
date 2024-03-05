from django.shortcuts import render,redirect
from django.views.generic import View
from reminderapp.forms import RegisterForm,LoginForm,TodoForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from reminderapp.models import Todos
from django.utils.decorators import method_decorator
from reminderapp.decorators import signin_required,owner_permission_required
# Create your views here.


all_decorators=[signin_required,owner_permission_required]

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,'register.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()  #autosave to db, RegisterForm inherited from UserCreationForm which def save() function
            messages.success(request,'Account created successfully')
            return redirect('login')
        else:
            messages.error(request,'Failed to create an account')
            return render(request,'register.html',{'form':form})
        

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get('username')
            pass_word=form.cleaned_data.get('password')
            user_object=authenticate(request,username=user_name,password=pass_word)
            if user_object:
                login(request,user_object)
                messages.success(request,'Successfully logged in')
                return redirect('home')
            messages.error(request,'Invalid credential')
            return render(request,'login.html',{'form':form})
        
@method_decorator(signin_required,name='dispatch')
class HomeView(View):
    def get(self,request,*args,**kwargs):
        form=TodoForm()
        user_data=Todos.objects.filter(user=request.user).order_by('status')
        return render(request,'home.html',{'form':form,'user_data':user_data})
    
    def post(self,request,*args,**kwargs):
        form=TodoForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user  #form.instance.user=Todo.user in models.py
            form.save()
            messages.success(request,'Todo added!')
            return redirect('home')
        else:
            return render(request,'home.html',{'form':form})

#localhost/todos/{id}/remove/ 
@method_decorator(all_decorators,name='dispatch')           
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Todos.objects.filter(id=id).delete()
        messages.success(request,'Deleted this To Do!')
        return redirect('home')
    
#localhost/todos/{id}/change/
@method_decorator(all_decorators,name='dispatch')
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        # Todos.objects.filter(id=id).update(status=True)
        todo_object=Todos.objects.get(id=id)
        if todo_object.status==True:
            todo_object.status=False
            todo_object.save()
            messages.success(request,'This To Do not finished!')
        else:
            todo_object.status=True
            todo_object.save()
            messages.success(request,'This To Do has been finished')
        return redirect('home')
         
@method_decorator(signin_required,name='dispatch')           
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,'Logged out!')
        return redirect('login')