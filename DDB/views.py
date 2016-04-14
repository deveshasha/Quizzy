from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

class HomePage(generic.TemplateView):
    template_name = "home.html"

def home(request):
	return render(request, 'base.html')

