# shop/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, CustomerCreateView
from .views import CulqiChargeView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', CustomerCreateView.as_view(), name='customer-register'),
     path('api/culqi/charge/', CulqiChargeView.as_view(), name='culqi-charge'),
]
    