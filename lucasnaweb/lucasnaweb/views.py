from django.shortcuts import render, get_object_or_404
from blog.models import Page
from .forms import ContactForm
# Create your views here.

def about(request):
    page = get_object_or_404(Page, slug='sobre')
    return render(request, 'about.html',{'page':page})

def contact(request):
    form_class = ContactForm
    page = get_object_or_404(Page, slug='contato')
    return render(request, 'contato.html',{'form':form_class, 'page':page})