from django.urls import path
from .views import tblSupervCanchaListCreateView

urlpatterns = [
    path('', tblSupervCanchaListCreateView.as_view(), name='list_create'),
]
