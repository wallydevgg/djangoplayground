from django.urls import path
from .views import tblSupervCanchaListCreateView, tblPersSeguridadListCreateView

urlpatterns = [
    path("supervisorcancha/", tblSupervCanchaListCreateView.as_view(), name="list_create"),
    path("peronalseguridad/", tblPersSeguridadListCreateView.as_view(), name="security_list_create"),
]
