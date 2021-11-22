import re, json

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View
from django.db              import DataError

from .models                import User  

def regex_match(regex, value):   
    if not re.match(regex, value):
        raise ValidationError(f"{value} INVALID_USER")
    
  
def email_exists(email):
    if User.objects.filter(email).exists():
        raise ValidationError("USER_ALREADY_EXISTS")   
    
def pw_validation(password):
    if (password != data['password']):
        raise ValidationError("INVALID_PASSWORD")
    