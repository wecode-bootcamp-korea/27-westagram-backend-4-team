import re, json

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View
from django.db              import DataError

from .models                import User    

class SignUpView(View):
    def post(self,request):
        try:
            data           = json.loads(request.body)
            email          = data["email"]
            password	   = data["password"]
            email_regex    = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            password_regex = "^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$"
            
            if not re.match(email_regex, email):
                raise ValidationError("INVALID_EMAIL")
            
            if not re.match(password_regex, password):
                raise ValidationError("INVALID_PASSWORD") 
            
            if User.objects.filter(email).exists():
                raise ValidationError("USER_ALREADY_EXISTS") 
            
            User.objects.create(
                name          = data["name"],
                email         = email,
                password      = password,
                phone_number  = data["phone_number"],
                information   = data.get("info"),
             )

            return JsonResponse({"message" : "SUCCESS"}, status=201) 
        
        except ValidationError as e:
            return JsonResponse({"message":e.message}, status=401)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        
        except DataError:
            return JsonResponse({"message":"DATA_ERROR"}, status=401)
