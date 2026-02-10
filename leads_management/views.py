from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ser import form_dataserializer
from .models import form_data
from rest_framework import status, permissions
from rest_framework.views import APIView


# Create your views here.


class submit_form(APIView):


    def post(self, request):
        serializer=form_dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    