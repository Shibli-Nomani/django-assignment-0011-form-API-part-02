from django.urls import path
from . import views

urlpatterns = [
    path('attraction/', views.Attractions, name ='attractions'),
    path('blogs/', views.Blogs, name ='blogs'),
]