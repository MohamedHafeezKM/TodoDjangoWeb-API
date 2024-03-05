from django.forms import ModelForm,TextInput,PasswordInput,EmailInput,Form,CharField,Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from reminderapp.models import Todos



class RegisterForm(UserCreationForm):
    password1=CharField()  #did this to visible one password
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

        widgets={
            'username':TextInput(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
            'password1':TextInput(attrs={'class':'form-control'}),
            'password2':PasswordInput(attrs={'class':'form-control'})
        }

class LoginForm(Form):
    username=CharField(widget=TextInput(attrs={'class':'form-control'}))
    password=CharField(widget=PasswordInput(attrs={'class':'form-control'}))

class TodoForm(ModelForm):
    class Meta:
        model=Todos
        fields=['name']

  