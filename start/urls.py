from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('automated_consultancy', views.automated_consultancy, name = "AC" ),
    path('cost', views.estimated_cost, name = "cost" ),
    path('bid', views.bidding, name='bid'),
    path('blog', views.blog, name='blog'),
    path('popup', views.popup, name="popup"),
]