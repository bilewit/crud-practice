from django.shortcuts import render
from django.http import JsonResponse
from funapi import models
from funapi  import serializers
from rest_framework.decorators import api_view
from rest_framework.response import responses, Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = models.Drink.objects.all()
        serializer = serializers.DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, pk,format=None):

    try:
        drink = models.Drink.objects.get(pk=pk)
    except models.Drink.DoesNotExist:
        pass

    if request.method == 'GET':

        serializer = serializers.DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

