from django.urls import path
from .views import RegisterView, LoginView, RefreshView, ResetPasswordView

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(), name="signin"),
    path("token/refresh/", RefreshView.as_view(), name="token_refresh"),
    path("reset_password", ResetPasswordView.as_view(), name="reset_password"),
]
