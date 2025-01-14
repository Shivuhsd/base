from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('home/gemini/', include('home.urls')),
]