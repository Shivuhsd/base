from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.GeminiSearchView.as_view(), name='search'),

    path('feedback/', views.UserFeedbackView.as_view(), name='feedback'),
]