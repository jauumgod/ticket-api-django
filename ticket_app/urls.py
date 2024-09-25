from django.urls import path
from .views import (
    UserListCreateView,UserRetrieveUpdateDestroyView,
    TicketsListCreateView, TicketsRetrieveUpdateDestroyView,
    EmpresasListCreateView, EmpresasRetrieveUpdateDestroyView,
)
from .views import CustomTokenObtainPairView


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users-list'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users-detail'),
    path('tickets/', TicketsListCreateView.as_view(), name='tickets-list'),
    path('tickets/<int:pk>', TicketsRetrieveUpdateDestroyView.as_view(), name='tickets-detail'),
    path('operacoes/', EmpresasListCreateView.as_view(), name='operacao-list'),
    path('operacoes/<int:pk>', EmpresasRetrieveUpdateDestroyView.as_view(), name='tickets-detail'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

