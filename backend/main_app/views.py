from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    view = TemplateView.as_view(template_name='main/home.html')
    return view(request)