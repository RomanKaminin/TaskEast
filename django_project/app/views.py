from django.views.generic import ListView, DetailView
from app.models import Client, Department
from django.shortcuts import get_object_or_404, render
from django_filters.views import FilterView
from app.filtersets import ClientFilter


# class ClientList(ListView):
#     context_object_name = 'clients_list'
#     template_name = "home.html"
#
#     def get_queryset(self):
#         clients = Client.objects.all()
#         queryset = get_records(self.request, clients, 2)
#         return queryset


# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = Client
#         fields = ['department', 'end_work_date']

class ClientList(FilterView):
    context_object_name = 'clients_list'
    template_name = "home.html"
    paginate_by = 2
    model = Client
    filter_class = ClientFilter
    filterset_fields = {'department', 'username'}


class ClientDetail(ListView):
    context_object_name = 'client_data'
    template_name = 'client_detail.html'

    def get_queryset(self):
        self.client = get_object_or_404(Client, id=self.kwargs['pk'])
        return self.client


