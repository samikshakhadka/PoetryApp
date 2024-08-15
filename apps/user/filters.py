from django_filters import rest_framework as filters
from .models import CustomUser

class CustomUserFilter(filters.FilterSet):
    email = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    date_joined = filters.DateFromToRangeFilter()
    # is_verified = filters.BooleanFilter()
    # is_staff = filters.BooleanFilter()

    class Meta:
        model = CustomUser
        fields = ['email','first_name', 'last_name', 'date_joined']
