from django.urls import path, include

urlpatterns = [
    path('merchant/', include('merchant.urls')),
    path('user/', include('Buyer.urls')),
    path('authentication/', include('auuth.urls')),
    path('home/', include('home.urls')),
]