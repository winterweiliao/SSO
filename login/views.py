import json
import base64

from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView


# Create your views here.
def login_page(request):
    return render(request, 'login/login_page2.html')


def login_success_page(request):
    token = request.GET.get('token')
    app_url = request.GET.get('app_url')
    return render(request, 'login/login_success_page.html', {'token': token, 'app_url': app_url})


def login_redirect(request):
    app_url = request.GET.get('app_url')
    token = request.GET.get('token')
    url = '%s?token=%s' % (app_url, token)
    return redirect(url)


def login_logout(request):
    return redirect('/')


class LoginSuccessAPIView(APIView):
    """
    """
    def post(self, request, *args, **kwargs):
        jwt = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        payload = jwt.split(".")[1]
        payload = base64.urlsafe_b64decode(payload + '=' * (4 - len(payload) % 4))
        payload = json.loads(payload)
        return JsonResponse({'token': jwt, 'payload': payload})
