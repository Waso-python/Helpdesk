from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "helpdesk/base.html"