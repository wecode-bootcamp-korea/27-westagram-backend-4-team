from django.shortcuts import render

# Create your views here.

import json, re

from django.http     import JsonResponse
from django.views    import View

from users.models    import User

class SignUpView(View):
    def post(self, request):

        try:
            data = json.loads(request.body)


            regexp_email    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            regexp_password = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')

            if re.match(regexp_email, data['email']) is None:
                return JsonResponse({'message' : 'WRONG_EMAIL_FORMAT'}, status=400)

            if re.match(regexp_password, data['password']) is None:
                return JsonResponse({'message' : 'WRONG_PASSWORD_FORMAT'}, status=400)

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message' : 'USER_ALREADY_EXISTS'}, status=400)

            if re.match(regexp_email, data['email']) and re.match(regexp_password, data['password']):

                 User.objects.create(
                     name        = data['name'],
                     email       = data['email'],
                     password    = data['password'],
                     contacts    = data['contacts'],
                     address     = data['address']
                 )

                 return JsonResponse({'message' : 'CREATED'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)


class LoginView(View):
    def post(self, request):
        data     = json.loads(request.body)
        email    = User.objects.filter(email = 'email')
        password = User.objects.filter(password = 'password')

        try:

            if email.exists() and password.exists():
                return JsonResponse({"message" : "SUCCESS"}, status=200)

            else:
                return JsonResponse({"message" : "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message" : "USER_DOESNT_EXIST"}, status=400)
