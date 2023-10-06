from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.ProductSearchView.as_view()),
    path('products/', views.ProductList.as_view()),
]