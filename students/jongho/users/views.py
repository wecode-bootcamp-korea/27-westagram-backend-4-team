import json,re

from django.views import View
from django.http  import JsonResponse
from django.db    import IntegrityError

from .models      import User

class UserInformaiton(View):

  def post(self,request):
    try:
      data                   = json.loads(request.body)
      email_confirm_regex    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
      password_confirm_regex = '^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$'
      
      if re.match(email_confirm_regex,data["email"]) and re.match(password_confirm_regex,data["password"]):
        User.objects.create(
          name        = data["name"],
          email       = data["email"],
          password    = data["password"],
          phone       = data["phone"],
          information = data["information"]
        )
        return JsonResponse({'message':"CREATE"},status=201)

      return JsonResponse({'message':"INVALID_USER"},status=400)
    
    except KeyError:
      return JsonResponse({'message':"KEYERROR"},status=400)

    except IntegrityError:
      return JsonResponse({'message':"INTERGRITYERROR"},status=400)

    
# Create your views here.
