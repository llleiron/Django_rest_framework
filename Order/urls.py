from django.urls import path
from Order.views import(
    OrderCreateAPIView,
    OrderListAPIView,
    OrderDetailAPIView
)

urlpatterns = [
path('create', OrderCreateAPIView.as_view()),
path('all', OrderListAPIView.as_view()),
path('detail/<int:pk>', OrderDetailAPIView.as_view())
]