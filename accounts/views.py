from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status

# Create your views here.
class RegisterList(APIView):
    def post(self, request, format=None):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        password2 = request.data['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                response = {
                        "Status": False,
                        "Message": "username Already Exit.",
                    }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                if User.objects.filter(email=email).exists():
                    response = {
                        "Status": False,
                        "Message": "Email Already Exit.",
                    }
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    response = {
                            "Status": True,
                            "Message": "Successfully registered",
                        }
                    return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                    "Status": False,
                    "Message": "Password is not Matching",
                }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        