from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmListAPIView.as_view()),
    path('<int:pk>/', views.FilmDetailAPIView.as_view()),
]