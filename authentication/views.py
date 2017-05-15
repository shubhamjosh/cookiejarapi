from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
import json

class SignUp(View):

    def post(self, request):
        request_body = json.loads(request.body.decode('utf-8'))
        user_first_name = request_body["first_name"]
        user_last_name = request_body["last_name"]
        user_email_address = request_body["email"]
        user_password = request_body["password"]

        user = User.objects.create_user(username=user_email_address, first_name=user_first_name, last_name=user_last_name,\
                                        email=user_email_address, password=user_password )

        return HttpResponse(user)

class LogIn(View):
    def get(self, request, username):
        request_body = json.loads(request.body.decode('utf-8'))
        # user_username = request.body['username']
        # user_password = request.body['password']

        return HttpResponse("OK!")
