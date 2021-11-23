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
            if re.match(email_regex,data['email']) and re.match(password_regex,data['password']):
                User.objects.create(
                name      = data['name'],
                email     = data['email'],
                password  = data['password'],
                call_num  = data['call_num'],
                address   = data.get("address",""),
                )
                return JsonResponse({'message':'CREATE'}, status=201)
            return JsonResponse({"message": "CHECK_VALUE"})
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"},status=400)