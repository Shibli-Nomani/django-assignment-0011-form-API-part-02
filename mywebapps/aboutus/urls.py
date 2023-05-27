from django.urls import path
from . import views

urlpatterns = [
    path('', views.About_Us, name='aboutus'),
    path('profiles/', views.Profiles, name ='profiles'),
    path('portfolio/', views.portfolio, name ='protfolio'),
]