import re

from django.core.exceptions import ValidationError

from .models                import User  

email_regex    = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
password_regex = "^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$"

def regex_match(regex, value):   
    if not re.match(regex, value):
        raise ValidationError(f"{value} INVALID_USER")
  
def email_exists(email):
    if User.objects.filter(email).exists():
        raise ValidationError("USER_ALREADY_EXISTS")   
    
def pw_validation(password):
    if (password != data['password']):
        raise ValidationError("INVALID_PASSWORD")
    