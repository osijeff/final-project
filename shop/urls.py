from django.urls import path

from . import views
from .views import * 
# HomePageView, AboutPageView, ContactPageView, BlogPageView, TrackerPageView



urlpatterns = [
    path('cart/', CartPageView.as_view(), name='cart'),
    path('checkout/',  CheckoutPageView.as_view(), name='checkout'),
    path('tracker/', TrackerPageView.as_view(), name='tracker'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    
]