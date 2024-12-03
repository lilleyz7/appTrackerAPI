from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'title', 'company', 'details', 'location', 'listing', 'added', 'deadline', 'status']