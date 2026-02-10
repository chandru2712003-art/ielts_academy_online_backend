
#import the necessary libraries
from rest_framework import serializers
from .models import form_data


# Create a serializer for the form_data model
class form_dataserializer(serializers.ModelSerializer):
    class Meta:
        model = form_data
        fields = '__all__'