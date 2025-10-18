from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request):
    return Response({'status': 'ok', 'api': '/api/'})


urlpatterns = [
    path('', api_root, name='api_root'),
    path('api/', include('octofit_tracker.api_urls')),
]
