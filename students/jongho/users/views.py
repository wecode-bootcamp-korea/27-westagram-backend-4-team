import json,re

from django.views import View
from django.http  import JsonResponse
from django.db    import DataError

from .models      import User

class SignUp(View):
  def post(self,request):
    try:
      data                = json.loads(request.body)
      EMAIL_REGEX         = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
      PSSWORD_REGEX       = '^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$'

      if not re.match(EMAIL_REGEX,data["email"]):
        return JsonResponse({'message':"INVALID_EMAIL"},status=400)
      
      if not re.match(PSSWORD_REGEX,data["password"]):
        return JsonResponse({'message':"INVALID_PASSWORD"},status=400)

      if User.objects.filter(email=data["email"]).exists():
        return JsonResponse({'message':"INVALID_ETGIKEUL"},status=400)

      User.objects.create(
        name         = data["name"],
        email        = data["email"],
        password     = data["password"],
        phone_number = data["phone"],
        information  = data.get("information","")
      )
      return JsonResponse({'message':"CREATE"},status=201)

    except KeyError:
      return JsonResponse({'message':"KEYERROR"},status=400)
    
    except DataError:
      return JsonResponse({"message":"DATAERROR"},status=401)