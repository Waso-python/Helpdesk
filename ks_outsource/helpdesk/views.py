import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import OrgUserForm
from .models import OrgUser, Ticket


class JSONListView(ListView):
    model = OrgUser
    queryset = OrgUser.objects.order_by('org')
    template_name = "helpdesk/orguser_list.html"

class TicketListView(ListView):
    model = Ticket
    template_name = "helpdesk/ticket_list.html"

# class JSONDetailView(DetailView):
#     model = OrgUser
#     template_name = "helpdesk/orguser_detail.html"

# class JSONUpdate(UpdateView):
#     model = OrgUser
#     form_class = OrgUserForm
# #    fields = ['name', 'data']
#     template_name = "helpdesk/OrgUser_update.html"


# class JSONDelete(DeleteView):
#     model = OrgUser
#     template_name = "helpdesk/OrgUser_delete.html"
#     success_url = reverse_lazy('OrgUserlist')


# class ContactView(FormView):
#     template_name = 'helpdesk/contact.html'
#     form_class = OrgUserForm
#     success_url = '/thanks/'


class OrgUserCreate(CreateView):
    model = OrgUser
    form_class = OrgUserForm
    template_name = "helpdesk/testcreate.html"
    success_url = '/thanks/'


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
