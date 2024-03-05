from django.urls import path
from api import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router2=DefaultRouter()
router.register('todos',views.TodosViewSet,basename='todos')

router2.register('todos2',views.TodosModelViewSet,basename='todos2')



urlpatterns=[
    path('register/',views.SignUpView.as_view()),
    path('generate-token/',ObtainAuthToken.as_view()),

]+router.urls+router2.urls