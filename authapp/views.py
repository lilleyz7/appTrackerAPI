# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from .serializers import UserSerializer
# from .models import CustomUser
# from rest_framework import status

# # Create your views here.

# @api_view(['POST'])
# def registration_view(request):
#     try:
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = CustomUser.objects.get(username=request.data['username'])
#             user.set_password(request.data['password'])
#             user.save()
#             return Response({'user': serializer.data},
#                                 status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)