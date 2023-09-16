from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'', views.FilmViewSet)

urlpatterns = [
    # path('', views.FilmListAPIView.as_view()),
    # path('<int:pk>/', views.FilmDetailAPIView.as_view()),
    # path('', views.FilmViewSet.as_view({'get': 'list'})),
    # path('<int:pk>/', views.FilmViewSet.as_view({'get': 'retrieve'})),
    path('', include(router.urls)),
]