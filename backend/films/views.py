from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.
class FilmListAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer



class FilmAPIView(APIView):
    def get(self, request):
        films = Film.objects.all()
        return Response({'film': FilmSerializer(films, many=True).data})
    
    def post(self, request):
        # new_film = Film.objects.create(
        #     poster=request.data['poster'],
        #     title_ru=request.data['title_ru'],
        #     title_orig=request.data['title_orig'],
        #     prod_year=request.data['prod_year'],
        #     timing=request.data['timing'],
        #     premiere_date=request.data['premiere_date'],
        #     country_id=request.data['country_id'],
        #     genre_id=request.data['genre_id'],
        #     director_id=request.data['director_id'],
        # )
        # new_film.save()

        # return Response({'film': FilmSerializer(new_film).data})

        serializer = FilmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'film': serializer.data})
    

    def put(self, request, *args, **kwargs):        # Обновить данные 
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method "PUT" not allowed.'})
        
        try:
            instance = Film.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists.'})
        
        serializer = FilmSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'film': serializer.data})
    

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method "DELETE" not allowed.'})
        
        try:
            instance = Film.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Object does not exists.'})
        
        return Response({'status': 'Film was deleted.'})