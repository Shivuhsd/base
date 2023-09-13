from django.urls import path
from .views import MymodelListView

urlpatterns = [
    path('', MymodelListView.as_view(), name='mymodel'),
]