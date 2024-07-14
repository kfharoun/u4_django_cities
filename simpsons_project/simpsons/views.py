from django.shortcuts import render
from rest_framework import generics
from .serializers import CitySerializer, ReviewSerializer, AttractionSerializer
from .models import City, Review, Attraction

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class AttractionList(generics.ListCreateAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

class AttractionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer