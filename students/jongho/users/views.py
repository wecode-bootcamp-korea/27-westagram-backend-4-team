import json

from django.views           import View
from django.http            import JsonResponse
from django.db              import DataError
from django.core.exceptions import ValidationError

from .models      import User
from .my_module   import email_regex,password_regex

class SignUpView(View):
  def post(self,request):
    try:
      data = json.loads(request.body)
      email_regex(data)
      password_regex(data)
      
      if User.objects.filter(email=data["email"]).exists():
         return JsonResponse({'message':"email_already_exists"},status=400)
         
      User.objects.create(
      name         = data["name"],
      email        = data["email"],
      password     = data["password"],
      phone_number = data["phone_number"],
      information  = data.get("information","")
    )
      return JsonResponse({'message':"CREATE"},status=201)

    except KeyError:
      return JsonResponse({'message':"KEYERROR"},status=400)
    
    except DataError:
      return JsonResponse({"message":"DATAERROR"},status=401)
    
    except ValidationError as e:
      return JsonResponse({"message":e.message},status=401)

class SignInView(View):
  def post(self,request):
    try:
      data = json.loads(request.body)
      email_regex(data) #DB hit전에 정규표현식 검사
      password_regex(data)
      user = User.objects.get(email=data["email"])

      if data["password"] == user.password and data["email"] == user.email:
        return JsonResponse({'message':"SUCCESS"},status=200)

      return JsonResponse({'message':"INVALID_PASSWORD"},status=401)

    except KeyError:
      return JsonResponse({'message':"KEYERROR"},status=400)
    
    except User.DoesNotExist:
      return JsonResponse({'message':"INVALID_EMAIL"},status=401)
    
    except ValidationError as e:
      return JsonResponse({"message":e.message},status=401)