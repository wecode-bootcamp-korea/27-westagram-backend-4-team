import re

from django.core.exceptions import ValidationError

EMAIL_REGEX         = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PSSWORD_REGEX       = '^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$'
def email_regex(data):
  if not re.match(EMAIL_REGEX,data["email"]):
    raise ValidationError("INVALID_EMAIL")

def password_regex(data): 
  if not re.match(PSSWORD_REGEX,data["password"]):
    raise ValidationError("INVALID_PASSWORD")