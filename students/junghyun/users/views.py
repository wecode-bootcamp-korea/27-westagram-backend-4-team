import json

from .validator             import *
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View
from django.db              import DataError

from .models                import User    

class SignUpView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            email          = data["email"]
            password	   = data["password"]
            
            regex_match(email_regex, email)
            regex_match(password_regex, password)
            email_exists(email)
            
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
        
class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            password = User.objects.get(email = data['email']).password
            pw_validation(password)
            return JsonResponse({'message':'SUCCESS'},status = 200)
        
        except ValidationError as e:
            return JsonResponse({'message':e.message}, status = 401)
        
        except ObjectDoesNotExist:
            return JsonResponse({'message':'INVALID_EMAIL'}, status=401)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status = 400)        
