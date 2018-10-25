from django.views.generic import ListView, DetailView
from app.models import Client, Department
from django.shortcuts import get_object_or_404, render
from app.helpers import get_records


# class ClientList(ListView):
#     context_object_name = 'clients_list'
#     template_name = "home.html"
#
#     def get_queryset(self):
#         clients = Client.objects.all()
#         queryset = get_records(self.request, clients, 2)
#         return queryset

class ClientList(ListView):
    context_object_name = 'clients_list'
    template_name = "home.html"
    paginate_by = 2


    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Client.objects.filter(category=self.kwargs['category']).order_by('-createdAt')
        else:
            query = Client.objects.all().order_by('id')
            return query





class ClientDetail(ListView):
    context_object_name = 'client_data'
    template_name = 'client_detail.html'

    def get_queryset(self):
        self.client = get_object_or_404(Client, id=self.kwargs['pk'])
        return self.client

