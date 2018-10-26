import django_filters
from app.models import Client


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['department', 'end_work_date']

