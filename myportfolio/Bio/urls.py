
from django.urls import path
from Bio import views

urlpatterns = [
    path('base/',views.base, name='base' ),
    path('',views.home, name='home' ),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blogs,name='blog'),
]
