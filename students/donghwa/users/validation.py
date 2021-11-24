import re

from django.core.exceptions import ValidationError

def regexp_email_confirm(email):
    regexp_email = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not re.match(regexp_email, email):
        raise ValidationError("INVALID_EMAIL")

def regexp_password_confirm(password):
    regexp_password = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
    if not re.match(regexp_password, password):
        raise ValidationError("INVALID_PASSWORD")
