import django_filters
from app.models import Client


class ClientFilter(django_filters.FilterSet):

    VALUES_WOR = (
        ('true', 'Работают'),
        ('false', 'Не работают')
    )
    now_work = django_filters.ChoiceFilter(
        label='Работает в компании',
        choices=VALUES_WOR,
        method='filter_by_end_work'
    )

    VALUES_ORD =(
        ('asc', 'ASC'),
        ('desc', 'DESC')
    )
    ordering = django_filters.ChoiceFilter(
        label='Порядок',
        choices=VALUES_ORD,
        method='filter_by_order'
    )

    class Meta:
        model = Client
        fields = ['department',]

    def filter_by_order(self, queryset, name, value):
        expression = 'first_name' if value == 'asc' else '-first_name'
        return queryset.order_by(expression)

    def filter_by_end_work(self, queryset, name, value):
        if value == 'true':
           query = queryset.filter(end_work_date__isnull=True)
        else:
            query = queryset.filter(end_work_date__isnull=False)
        return query


