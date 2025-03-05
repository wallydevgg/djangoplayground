from django.urls import path
from .views import CouponListCreateAPIView, CouponRetrieveUpdateDestroyAPIView

urlpatterns = [
  path("coupons/", CouponListCreateAPIView.as_view(), name="coupon-list-create"),
  path("coupons/<int:id>/", CouponRetrieveUpdateDestroyAPIView.as_view(), name="coupon-retrieve-update-destroy"),
]