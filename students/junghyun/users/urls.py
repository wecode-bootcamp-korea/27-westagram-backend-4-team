
from django.urls import path

from users.views  import SignupView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
]
