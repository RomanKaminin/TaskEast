from django.views.generic import ListView
from app.models import Client
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView
from app.filtersets import ClientFilter, AlphabetFilter
from app.helpers import paginator_work
from urllib.parse import urlencode


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
    filter_class = AlphabetFilter

    def get_context_data(self, **kwargs):
        qs = self.model.objects.all()
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
        return context
