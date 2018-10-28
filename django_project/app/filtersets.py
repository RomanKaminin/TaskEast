import django_filters
from app.models import Client
from django.db.models import Q

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
        expression = 'username' if value == 'asc' else '-username'
        return queryset.order_by(expression)

    def filter_by_end_work(self, queryset, name, value):
        if value == 'true':
           query = queryset.filter(end_work_date__isnull=True)
        else:
            query = queryset.filter(end_work_date__isnull=False)
        return query


class AlphabetFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = []

    FIRST_VALUES = (
        (u'а_б_в_г', 'А-Г'),
        (u'а', 'А'),
        (u'б', 'Б'),
        (u'в', 'В'),
        (u'г', 'Г'),
    )
    first_alph = django_filters.ChoiceFilter(
        label='А-Г',
        choices=FIRST_VALUES,
        method='filter_alph'
    )

    SECOND_VALUES = (
        (u'д_е_ё_ж', 'Д-Ж'),
        (u'д', 'Д'),
        (u'е', 'Е'),
        (u'ё', 'Ё'),
        (u'ж', 'Ж'),
    )
    second_alph = django_filters.ChoiceFilter(
        label='Д-Ж',
        choices=SECOND_VALUES,
        method='filter_alph'
    )

    THIRD_VALUES = (
        (u'з_и_й_к', '3-К'),
        (u'з', 'З'),
        (u'и', 'И'),
        (u'й', 'Й'),
        (u'к', 'К'),
    )
    third_alph = django_filters.ChoiceFilter(
        label='З-К',
        choices=THIRD_VALUES,
        method='filter_alph'
    )

    FOURTH_VALUES = (
        (u'л_м_н_о_п', 'Л-П'),
        (u'л', 'Л'),
        (u'м', 'М'),
        (u'н', 'Н'),
        (u'о', 'О'),
        (u'п', 'П'),
    )
    fourth_alph = django_filters.ChoiceFilter(
        label='Л-П',
        choices=FOURTH_VALUES,
        method='filter_alph'
    )

    FIFTH_VALUES = (
        (u'р_с_т_у', 'Р-У'),
        (u'р', 'Р'),
        (u'с', 'С'),
        (u'т', 'Т'),
        (u'у', 'У'),
    )
    fifth_alph = django_filters.ChoiceFilter(
        label='Р-У',
        choices=FIFTH_VALUES,
        method='filter_alph'
    )

    SIXTH_VALUES = (
        (u'ф_х_ц_ч_ш', 'Ф-Ш'),
        (u'ф', 'Ф'),
        (u'х', 'Х'),
        (u'ц', 'Ц'),
        (u'ч', 'Ч'),
        (u'ш', 'Ш'),
    )
    sixth_alph = django_filters.ChoiceFilter(
        label='Ф-Ш',
        choices=SIXTH_VALUES,
        method='filter_alph'
    )

    SEVENTH_VALUES = (
        (u'щ_э_ю_я', 'Щ-Я'),
        (u'щ', 'Щ'),
        (u'э', 'Э'),
        (u'ю', 'Ю'),
        (u'я', 'Я'),
    )
    seventh_alph = django_filters.ChoiceFilter(
        label='Щ-Я',
        choices=SEVENTH_VALUES,
        method='filter_alph'
    )

    def filter_alph(self, queryset, name, value):
        if len(value) > 1:
            value_list = value.split("_")
            query = Client.objects.none()
            for i in value_list:
                query_feltred = queryset.order_by("first_name").filter(
                    Q(first_name__startswith=i) | Q(first_name__startswith=i.upper())
                )
                query = query.union(query_feltred)
        else:
            query = queryset.order_by("first_name").filter(
                Q(first_name__startswith=value) | Q(first_name__startswith=value.upper())
            )
        return query

