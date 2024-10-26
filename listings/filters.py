# products/filters.py
from django_filters import rest_framework as filters
from .models import Property

class PropertyFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Property
        fields = ['title', 'price_min', 'price_max']