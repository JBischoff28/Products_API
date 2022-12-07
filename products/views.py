from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import ProductsSerializer

@api_view(['GET', 'POST'])
def display_products(request):

    if request.method == 'GET':
        product = Products.objects.all()
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def select_product(request, pk):
    
    product = get_object_or_404(Products, pk=pk)    

    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
