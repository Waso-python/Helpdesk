import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import OrgUserForm 
from .models import OrgUser, Ticket, PhoneNumber


class JSONListView(ListView):
    model = OrgUser
    queryset = OrgUser.objects.order_by('org')
    template_name = "helpdesk/orguser_list.html"

class TicketListView(ListView):
    model = Ticket
    template_name = "helpdesk/ticket_list.html"


class OrgUserCreate(CreateView):
    model = OrgUser
    form_class = OrgUserForm
    template_name = "helpdesk/orguser_create.html"
    success_url = '/orguser/'

    def add_phone(self, user):
        phone_list = self.phones.replace(' ','').split(',')
        
        def save_phone(phone):
            phone = phone.replace(' ','')
            ph = PhoneNumber(user = user, phone = phone)
            ph.save()

        for it in phone_list:
            if it:
                save_phone(it)
    
    def form_valid(self, form):
        super().form_valid(form)
        self.add_phone(self.object)
        return redirect('orguser_list')

    def post(self, request, *args, **kwargs):
        self.phones = request.POST['phones']
        return super().post(self, request, *args, **kwargs)

class OrgUserDetailView(DetailView):
    model = OrgUser
    template_name = "helpdesk/orguser_detail.html"

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






    

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
