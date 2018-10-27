from django.views.generic import ListView
from app.models import Client
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView
from app.filtersets import ClientFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from app.helpers import get_records
from urllib.parse import urlencode


class ClientList(FilterView):
    template_name = "home.html"
    model = Client
    filter_class = ClientFilter

    def get_context_data(self, **kwargs):
        qs = self.model.objects.all()
        filtered = self.filter_class(self.request.GET, queryset=qs)
        qs_with_filters = filtered.qs
        paginator = Paginator(qs_with_filters, 3)
        page = self.request.GET.get('page')
        gt = self.request.GET.copy()
        if 'page' in gt:
            del gt['page']
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        context = {
            'paginator': paginator,
            'page_object': page_obj,
            'params': urlencode(gt),
            'filter': filtered,
        }
        return context



class ClientDetail(ListView):
    context_object_name = 'client_data'
    template_name = 'client_detail.html'

    def get_queryset(self):
        self.client = get_object_or_404(Client, id=self.kwargs['pk'])
        return self.client


