from django.views.generic import ListView
from app.models import Client
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView
from app.filtersets import ClientFilter
from app.helpers import paginator_work
from urllib.parse import urlencode
from django.db.models import Q
from django.conf import settings


class ClientList(FilterView):
    template_name = "home.html"
    model = Client
    filter_class = ClientFilter

    def get_context_data(self, **kwargs):
        qs = self.model.objects.all()
        if qs.exists():
            filtered = self.filter_class(self.request.GET, queryset=qs)
            qs_with_filters = filtered.qs
            paginator = paginator_work(self.request, qs_with_filters, 3)
            params = self.request.GET.copy()
            if 'page' in params:
                del params['page']
            context = {
                'paginator': paginator['paginator'],
                'page_objects': paginator['page_objects'],
                'params': urlencode(params),
                'filter': filtered,
            }
        else:
            context = {}
        return context

class ClientDetail(ListView):
    context_object_name = 'client_data'
    template_name = 'client_detail.html'

    def get_queryset(self):
        self.client = get_object_or_404(Client, id=self.kwargs['pk'])
        return self.client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_filter = self.request.build_absolute_uri()
        source_filter_page = url_filter[url_filter.find('?') + 1:]
        context['source_filter_page'] = source_filter_page
        return context


class AlphaList(ListView):
    template_name = 'alpha_detail.html'
    model = Client

    def get_context_data(self, **kwargs):
        qs = self.model.objects.all()
        if qs.exists():
            params = self.request.GET.copy()
            if 'page' in params:
                del params['page']

            values_alph = []
            if 'alph_val' in params:
                alph_literals = params['alph_val'][2:-2].split("-")
                alph_literals.extend(settings.VALUES_ALPH[len(settings.VALUES_ALPH) -
                                                          settings.VALUES_ALPH[::-1].index(alph_literals[0]):
                                                          settings.VALUES_ALPH.index(alph_literals[1])]
                                     )
                qs = self.model.objects.none()
                queryset = self.model.objects.all()

                for i in alph_literals:
                    query_feltred = queryset.order_by("first_name").filter(
                        Q(first_name__startswith=i) | Q(first_name__startswith=i.lower())
                    )
                    qs = qs.union(query_feltred)


            first_names = self.model.objects.all().values_list('first_name')
            first_names_list = [first_name[0][0] for first_name in first_names]
            for item in first_names_list:
                if item.upper() not in values_alph:
                    values_alph.append(item.upper())
            values_alph = sorted(values_alph)

            filters_alph = []
            if len(values_alph) > 4:
                number = 2
                if 4 < len(values_alph) <= 9:
                    number = 2
                elif 9 < len(values_alph) <= 13:
                    number = 3
                elif 13 < len(values_alph) <= 19:
                    number = 4
                elif 19 < len(values_alph) <= 25:
                    number = 5
                elif 25 < len(values_alph) <= 30:
                    number = 6
                elif  len(values_alph) > 30:
                    number = 7
                filter_alph_lists = self.split_alph_list(values_alph, number)
                for item_alph in filter_alph_lists:
                    filters_alph.append(['{}-{}'.format(item_alph[0], item_alph[-1])])
            else:
                filters_alph.append(['{}-{}'.format(values_alph[0], values_alph[-1])])

            paginator = paginator_work(self.request, qs.order_by('first_name'), 3)
            context = {
                'paginator': paginator['paginator'],
                'page_objects': paginator['page_objects'],
                'params': urlencode(params),
                'filters_alph': filters_alph,
            }
        else:
            context = {}

        return context

    def split_alph_list(self, a, n):
        k, m = divmod(len(a), n)
        return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


