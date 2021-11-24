import json, re

from django.http  import JsonResponse
from django.views import View

from users.models import User


class SignupView(View):
    def post(self,request):
        try:
            data           = json.loads(request.body)
            email_regex    = r'^[a-zA-Z0-9.-_]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
            password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}'
            
            if not re.match(email_regex,data['email']):
                return JsonResponse({'message':'INVALID_EMAIL'}, status=400)
            if not re.match(password_regex,data['password']):
                return JsonResponse({'message':'INVALID_PASSWORD'}, status=400)
            
            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = data['password'],
                phone_number  = data['phone_number'],
                address       = data.get('address','')
                )
            return JsonResponse({'message':'CREATE'}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email=data['email'])
            
            if not user:
                return JsonResponse({'message': 'INVALID_USER'}, status=400)
            if user.password == data['password']:
                return JsonResponse({'message':'SUCCESS'},status=200)
            return JsonResponse({'message':'INVALID_USER'},status=401)

        except User.DoesNotExist:
            return JsonResponse({'message':'EMAIL_ERROR'},status=401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)