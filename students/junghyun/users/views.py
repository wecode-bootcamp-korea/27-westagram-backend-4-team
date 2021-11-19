import re, json

from django.http      import JsonResponse
from django.views     import View
from django.db        import IntegrityError

from .models          import User

class SignUpView(View):
    def post(self,request):
        try:
            data                = json.loads(request.body)
            email               = data["email"]
            password            = data["password"]
            email_validation    = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            password_validation = "^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$"
            
            if re.match(email_validation, email) == None:
                return JsonResponse({"MESSAGE" : "EMAIL_VALID_ERROR"})
            
            if re.match(password_validation, password) == None:
                return JsonResponse({"MESSAGE" : "PASSWORD_VALID_ERROR"})
            
            User.objects.create(
                name         = data["name"],
                email        = data["email"],
                phone        = data["phone"],
                password     = data["password"],
                information  = data["info"],
            )
            
            return JsonResponse({"message" : "SUCCESS"}, status=201) 
        
        except IntegrityError:
            return JsonResponse({"message":"INTEGRITY_ERROR"}, status=400)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
