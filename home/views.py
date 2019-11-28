from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import UserProfile


# Create your views here.
def index(request):
    return render(request, 'home/index2.html')


class PlatFormAPIView(APIView):

    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        platform_groups = UserProfile.objects.get(user_id=user_id).platform_groups.all()
        data = {'platforms': []}
        for pg in platform_groups:
            platforms = pg.platforms.all()
            for p in platforms:
                platform = dict()
                platform['name'] = p.name
                platform['icon_url'] = p.icon_url
                platform['description'] = p.description
                platform['redirect_url'] = '%s?token=%s' % (p.redirect_url, str(request.auth))
                data['platforms'].append(platform)

        return JsonResponse(data)
