import re

from django.core.exceptions import ValidationError

EMAIL_REGEX         = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PSSWORD_REGEX       = '^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$'
def email_regex(email):
  if not re.match(EMAIL_REGEX,email):
    raise ValidationError("INVALID_EMAIL")

def password_regex(password): 
  if not re.match(PSSWORD_REGEX,password):
    raise ValidationError("INVALID_PASSWORD")