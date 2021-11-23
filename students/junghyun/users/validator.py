import re

from django.core.exceptions import ValidationError

def email_regex_match(email):   
    email_regex = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        raise ValidationError("EMAIL_INVALID")
    
def password_regex_match(password):   
    password_regex = "^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$"
    if not re.match(password_regex, password):
        raise ValidationError("PASSWORD_INVALID")
