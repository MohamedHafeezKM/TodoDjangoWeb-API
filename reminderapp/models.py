from django.db.models import Model,CharField,BooleanField,DateTimeField,ForeignKey,CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Todos(Model):
    name=CharField(max_length=200)
    date=DateTimeField(auto_now_add=True)
    user=ForeignKey(User,on_delete=CASCADE)
    status=BooleanField(default=False)

    def __str__(self):
        return self.name

