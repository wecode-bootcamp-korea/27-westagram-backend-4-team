import json

from django.http      import JsonResponse
from django.views     import View

from .models          import Posting
from users.models     import User

class SignUpView(View):
    def post(self, request):
        
        data = json.loads(request.body)
        user = User.objects.get(name=data['name']).name
        
        Posting.objects.create(
				user       = user,
    			image      = data['image'],
                text       = data['text'],
				created_at = 
				)
        
        return JsonResponse({'MESSAGE' : 'CREATED'}, status=201)
        