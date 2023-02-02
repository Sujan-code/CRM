from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views



router = DefaultRouter()
router.register('customerapi', views.CustomerModeViewset,basename="customer")
router.register('productapi', views.ProductModeViewset,basename="product")
router.register('orderapi', views.OrderModeViewset,basename="order")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]