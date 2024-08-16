from django_filters import rest_framework as filters
from .models import Poem

class PoemFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    poems = filters.CharFilter(lookup_expr='icontains')
    created_by = filters.NumberFilter(field_name='created_by__id') # no id
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()
    user = filters.NumberFilter(method= 'filter_by_user') # by user not necessary

    def filter_by_user(self, queryset,name,value):
        return queryset.filter(created_by__id=value)

    class Meta:
        model = Poem
        fields = ['title', 'author', 'poems', 'created_by', 'created_at', 'updated_at']