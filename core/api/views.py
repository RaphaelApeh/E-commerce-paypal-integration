from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from core.models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def productApi(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetailApi(request,pk):
    product = get_object_or_404(Product,id=pk)
    serailizer = ProductSerializer(product,many=False)
    return Response(serailizer.data)