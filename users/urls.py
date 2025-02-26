from django.urls import path
from .views import UserView, userGetByIdView, UserProfileView

urlpatterns = [
    path("", UserView.as_view(), name="list_create"),
    path("<int:id>", userGetByIdView.as_view(), name="read_update_delete"),
    path("profile/", UserProfileView.as_view(), name="profile_get_update"),
]
