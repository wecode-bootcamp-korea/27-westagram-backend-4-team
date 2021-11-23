import json, bcrypt, jwt

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View
from django.db              import DataError

from my_settings            import SECRET_KEY
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
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message":"USER_ALREADY_EXISTS"}, status = 401)
            
            User.objects.create(
                name          = data["name"],
                email         = email,
                password      = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode(),
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
            password = User.objects.get(email=data['email']).password
            if not bcrypt.checkpw(data['password'].encode('utf-8'), password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status = 401)
            return JsonResponse({'message':'SUCCESS',
                                'access_token' : jwt.encode({'id' : 1}, SECRET_KEY, algorithm = 'HS256')
                                }, status = 200)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status = 400) 
        
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_EMAIL'},status = 401) 