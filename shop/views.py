from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
#     return HttpResponse("<h1 style='color:red'>Hello, welcome to my store i hope you get what you are looking for.</h1>")


class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class ContactPageView(TemplateView):
    template_name = 'contact.html'
    
class BlogPageView(TemplateView):
    template_name = 'blog.html'
    
    
class TrackerPageView(TemplateView):
    template_name = 'tracker.html'
    
class CartPageView(TemplateView):
    template_name = 'cart.html'
    
class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'