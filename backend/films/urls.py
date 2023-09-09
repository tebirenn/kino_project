from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmAPIView.as_view()),
    path('<int:pk>/', views.FilmAPIView.as_view()),
]