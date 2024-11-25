from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# Create your views here.

@api_view(['POST'])
def register(request):
    return Response({'status': 'good'})