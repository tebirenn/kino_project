from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.
class FilmAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Побег из Шоушенка'})
    
    def post(self, request):
        print(request.data)
        return Response({'title': 'The Shawshank Redemption'})
    
