import re

from django.core.exceptions import ValidationError

def email_regex_match(email):   
    EMAIL_REGEX = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(EMAIL_REGEX, email):
        raise ValidationError("EMAIL_INVALID")
    
def password_regex_match(password):   
    PASSWORD_REGEX = "^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$"
    if not re.match(PASSWORD_REGEX, password):
        raise ValidationError("PASSWORD_INVALID")
