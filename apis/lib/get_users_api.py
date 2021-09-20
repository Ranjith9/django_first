from typing import Any
from apis.models import UserMetas
from rest_framework import views
from rest_framework.response import Response

class Users(views.APIView):
    def get(self, request, *args, **kwargs):
        result = []
        operation = request.query_params['operation']
        if operation == 'get_users':
            try:
                user_details = UserMetas.objects.all()
                for each in user_details:
                    result.append({
                        "name": each.name,
                        "email": each.email,
                        "designation": each.designation
                    })
            except Exception as e:
                result = str(e)
                
        return Response(result)