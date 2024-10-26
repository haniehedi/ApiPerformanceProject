from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import throttling
from .models import Agent,Property
from .serializers import PropertySerializer, AgentSerializer
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from .filters import PropertyFilter
from rest_framework.throttling import UserRateThrottle


class PropertySearchThrottle(UserRateThrottle):
    rate = '10000/minute'

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.select_related('agent').all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'price']
    filterset_class = PropertyFilter
    ordering_fields = ['title', 'price']
    ordering = ['title']

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        property_instance = serializer.save()
        cache.clear()

    def perform_update(self, serializer):
        property_instance = serializer.save()
        cache.clear()

    def perform_destroy(self, instance):
        instance.delete()
        cache.clear()

class AgentViewSet(ModelViewSet):
    queryset = Agent.objects.prefetch_related('properties').all()
    serializer_class = AgentSerializer
