from django.shortcuts import render
from django.template.response import TemplateResponse

def home(request):
    return TemplateResponse(request, 'pages/home.html', {})

def about(request):
    return TemplateResponse(request, 'pages/about.html', {})