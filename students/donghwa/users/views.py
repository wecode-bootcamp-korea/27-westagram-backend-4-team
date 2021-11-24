import re, json, bcrypt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from users.models           import User
from users.validation       import regexp_email_confirm, regexp_password_confirm

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            regexp_email_confirm(data['email'])
            regexp_password_confirm(data['password'])

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message' : 'USER_ALREADY_EXISTS'}, status=400)

            User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = hashed_password,
                contacts    = data['contacts'],
                address     = data['address']
            )

            return JsonResponse({'message' : 'CREATED'}, status=201)

        except ValidationError as e:
            return JsonResponse({'message' : e.message})

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)

            email   = User.objects.get(email = data['email'])

            if bcrypt.checkpw(data['password'].encode('utf-8'), email.password.encode('utf-8')):
                return JsonResponse({"message" : "SUCCESS"}, status=200)

            return JsonResponse({"message" : "INVALID_USER"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
