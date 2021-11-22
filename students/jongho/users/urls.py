from django.urls import path

from .views import UserInformaiton

urlpatterns = [
    path("/signup",UserInformaiton.as_view())
]