import json

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View
from django.db              import DataError

from .models                import User 
from .validator             import email_regex_match, password_regex_match   

class SignUpView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            email          = data["email"]
            password	   = data["password"]
            
            email_regex_match(email)
            password_regex_match(password)
            
            if User.objects.filter(email).exists():
                return JsonResponse({"message":"USER_ALREADY_EXISTS"}, status = 401)
            
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
            if not User.objects.filter(email=data['email'], password=data['password']).exists():
                return JsonResponse({'message': 'INVALID USER'}, status = 401)
            return JsonResponse({'message':'SUCCESS'},status = 200)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status = 400) 