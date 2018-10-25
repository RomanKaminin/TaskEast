from django.views.generic import ListView, DetailView
from app.models import Client, Department
from django.shortcuts import get_object_or_404

class ClientList(ListView):
    context_object_name = 'clients_list'
    queryset = Client.objects.all()
    template_name = "home.html"

# class ClientDetail(ListView):
#     context_object_name = 'client_data'
#     template_name = 'client_detail.html'
#
#     def get_queryset(self):
#
#         # self.client = get_object_or_404(Client, id=self.kwargs['pk'])
#         # raise Exception(self.client)
#         return Client.objects.filter(id=self.kwargs['pk'])
#
# def get_accesses(request):
#     list_groups = []
#     for g in request.user.groups.all():
#         list_groups.append(g.name)
#     if 'managers' in list_groups:
#         accesses = AccessRequest.objects.all()
#     else:
#         accesses = AccessRequest.objects.filter(name=request.user.username)
#     return render(request, 'accesses/accesses.html', {'accesses' : accesses})

class ClientDetail(DetailView):
    model = Client
    template_name = 'client_detail.html'

    def get_context_data(self, **kwargs):
        # self.client = get_object_or_404(Client, id=self.kwargs)
        context = super(ClientDetail, self).get_context_data(**kwargs)
        context['client_data'] = Client.objects.filter(username=kwargs)
        return context