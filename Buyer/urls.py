from django.urls import path
from . views import UserView, CartView, UserHistoryView, AddCart, UserAddressView

urlpatterns = [
    path('userinfo/<str:pk>/', UserView.as_view()),
    path('cart/<str:pk>/', CartView.as_view()),
    path('addcart/<str:pk>/', AddCart.as_view()),
    path('userhistory/<str:pk>/', UserHistoryView.as_view()),
    path('address/<str:pk>/', UserAddressView.as_view()),
]