from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Application
from .serializers import ApplicationSerializer
from django.core.cache import cache
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_applications_view(request):
    try:
        applications = Application.objects.filter(user=request.user)
    except Application.DoesNotExist:
        return Response({"error": "applications not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_application_by_id_view(request, pk):
    application = cache.get(f"single_app_{pk}")
    if not application:
        try:
            application = Application.objects.get(pk=pk, user=request.user)
            cache.set(f"single_app_{pk}", application, timeout=60*60)  
        except Application.DoesNotExist:
            return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ApplicationSerializer(application)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_application_view(request):
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(user=request.user)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_application_view(request, pk):
    application = cache.get(f"single_app_{pk}")
    if not application:
        try:
            application = Application.objects.get(pk=pk, user=request.user) 
            cache.set(f"single_app_{pk}", application, timeout=60*60)
        except Application.DoesNotExist:
            return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ApplicationSerializer(application, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        cache.delete(f"single_app_{pk}") 
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_application_view(request, pk):
    application = cache.get(f"single_app_{pk}")
    if not application:
        try:
            application = Application.objects.get(pk=pk, user=request.user) 
        except Application.DoesNotExist:
            return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

    cache.delete(f"single_app_{pk}")
    application.delete()
    return Response({"message": "Application deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

