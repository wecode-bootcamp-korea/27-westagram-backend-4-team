import re, json

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View
from django.db              import DataError

from .models                import User    

class SignUpView(View):
    def post(self,request):
        try:
            data                = json.loads(request.body)
            email               = data["email"]
            password            = data["password"]
            email_validation    = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            password_validation = "^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$"
            
            if re.match(email_validation, email) == None or re.match(password_validation, password) == None:
                raise ValidationError("INVALID_ERROR") 
            
            if User.objects.filter(email=data['email']).exists():
                raise ValidationError("INVALID_ERROR") 
            
            User.objects.create(
                name         = data["name"],
                email        = data["email"],
                phone_number  = data["phone_number"],
                password     = data["password"],
                information  = data["info"],
             )

            return JsonResponse({"message" : "SUCCESS"}, status=201) 
        
        except ValidationError:
            return JsonResponse({"message":"INVALID_ERROR"}, status=401)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        
        except DataError:
            return JsonResponse({"message":"DATA_ERROR"}, status=401)
