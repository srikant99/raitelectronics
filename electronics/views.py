from django.shortcuts import render
from .models import Page

# Create your views here.
def page(request):
    pages = Page.objects.all()
    return render(request, 'electronics/page.html', {'pages':pages})