from django_filters import rest_framework as django_filter

from api.models import Event


class EventsFilters(django_filter.FilterSet):
    min_date = django_filter.DateFilter(field_name='date', lookup_expr='gte')
    max_date = django_filter.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['min_date', 'max_date']
