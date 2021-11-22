from django.urls import path

from .views import UserInformaiton

urlpatterns = [
    path("/sginup",UserInformaiton.as_view())
]