# shop/views.py
from rest_framework import viewsets,  generics
from .models import Category, Product, Customer, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import status   
from rest_framework.views import APIView
from django.conf import settings
from culqi.client import Culqi
from culqi.resources import Charge


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


@api_view(['GET', 'POST'])
def registro_usuario(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
class CulqiChargeView(APIView):
    def post(self, request, *args, **kwargs):
        culqi = Culqi(settings.CULQI_SECRET_KEY)
        charge = Charge(culqi)
        
        data = {
            "amount": request.data.get("amount"),
            "currency_code": request.data.get("currency_code"),
            "email": request.data.get("email"),
            "source_id": request.data.get("source_id")
        }
        
        response = charge.create(data)
        return Response(response, status=status.HTTP_200_OK)
