import json
from django.views import View
from django.http  import JsonResponse
from .models      import User
import re
class UserInformaiton(View):

  def post(self,request):
    try:
      data             = json.loads(request.body)
      email_confirm    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
      password_confirm = re.compile('^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$')
      
      if email_confirm.match(data["email"]) and password_confirm.match(data["password"]):
        User.objects.create(
          name        = data["name"],
          email       = data["email"],
          password    = data["password"],
          phone       = data["phone"],
          information = data['information']
        )

        return JsonResponse({'message':"Create"},status=201)

      else:
        return JsonResponse({'message':"Id,Pw 확인"},status=400)
    
    except KeyError:
      return JsonResponse({'message':"KeyError"},status=400)
    
# Create your views here.
