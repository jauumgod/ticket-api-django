from django.urls import path
from .views import (
    UserListCreateView,UserRetrieveUpdateDestroyView,
    TicketsListCreateView, TicketsRetrieveUpdateDestroyView,
    OperacoesListCreateView, OperacoesRetrieveUpdateDestroyView,
    # SequenciaListCreateView, SequenciaRetrieveUpdateDestroyView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users-list'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users-detail'),
    path('tickets/', TicketsListCreateView.as_view(), name='tickets-list'),
    path('tickets/<int:pk>', TicketsRetrieveUpdateDestroyView.as_view(), name='tickets-detail'),
    path('operacoes/', OperacoesListCreateView.as_view(), name='operacao-list'),
    path('operacoes/<int:pk>', OperacoesRetrieveUpdateDestroyView.as_view(), name='tickets-detail'),
    # path('sequencia/', SequenciaListCreateView.as_view(), name='sequencia-list'),
    # path('sequencia/<int:pk>', SequenciaRetrieveUpdateDestroyView.as_view(), name='sequencia-detail'),
]

