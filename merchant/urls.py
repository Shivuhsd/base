from django.urls import path
from .views import MerchantStoreView, MerchantStoreUpdate, MerchantStoreCreateView

urlpatterns = [
    path('', MerchantStoreView.as_view(), name='merchant_store'),
    path('update/<str:pk>/', MerchantStoreUpdate.as_view(), name='merchant_update'),
    path('create/', MerchantStoreCreateView.as_view()),
]