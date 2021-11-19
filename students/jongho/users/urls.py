from django.urls import path
from .views import UserInformaiton

urlpatterns = [
    path("",UserInformaiton.as_view())
]