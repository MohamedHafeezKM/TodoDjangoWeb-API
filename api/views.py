from django.shortcuts import render
from django.contrib.auth.models import User
from api.serializers import UserSerializer,TodosSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from reminderapp.models import Todos

class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class TodosViewSet(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Todos.objects.filter(user=request.user)
        deserializer=TodosSerializer(qs,many=True)
        return Response(data=deserializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=TodosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Todos.objects.get(id=id)
        if qs.user==request.user:
            deserializer=TodosSerializer(qs)
            return Response(data=deserializer.data)
        else:
            raise serializers.ValidationError('Permission Denied!')

    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Todos.objects.get(id=id)
        
        if qs.user==request.user:
            qs.delete()
        else:
            raise serializers.ValidationError('Permission Denied!')
        

        return Response(data={'message':'This todo is deleted!'})
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        todo_object=Todos.objects.get(id=id)
        if todo_object.user==request.user:
            serializer=TodosSerializer(data=request.data,instance=todo_object)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
            
        else:
            raise serializers.ValidationError('Permission Denied!')
        

class TodosModelViewSet(ModelViewSet):
    queryset=Todos.objects.all()
    serializer_class=TodosSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs=Todos.objects.filter(user=self.request.user)
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


        
        
            
           
        



