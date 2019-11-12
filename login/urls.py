"""SSO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from .views import login_page, login_success_page, login_redirect, login_logout, LoginSuccessAPIView

urlpatterns = [
    path(r'api-token-auth/', obtain_jwt_token, name='login.obtain_jwt_token'),
    path(r'api-token-verify/', verify_jwt_token),
    path(r'login_page/', login_page, name='login.login_page'),
    path(r'login_success_page/', login_success_page, name='login.login_success_page'),
    path(r'login_redirect/', login_redirect, name='login.login_redirect'),
    path(r'login_success/', LoginSuccessAPIView.as_view(), name='login.login_success'),
    path(r'login_logout/', login_logout, name='login.login_logout'),
]
