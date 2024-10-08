from django.urls import path, include
from .views import (
    UserListCreateView,UserRetrieveUpdateDestroyView,
    TicketsListCreateView, TicketsRetrieveUpdateDestroyView,
    EmpresasListCreateView, EmpresasRetrieveUpdateDestroyView,
    ImagensViewSet
)
from .views import CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'imagens', ImagensViewSet, basename='imagens')

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users-list'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users-detail'),
    path('tickets/', TicketsListCreateView.as_view(), name='tickets-list'),
    path('tickets/<int:pk>', TicketsRetrieveUpdateDestroyView.as_view(), name='tickets-detail'),
    path('empresas/', EmpresasListCreateView.as_view(), name='operacao-list'),
    path('empresas/<int:pk>', EmpresasRetrieveUpdateDestroyView.as_view(), name='tickets-detail'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

