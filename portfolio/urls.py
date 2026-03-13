from django.urls import path
from .views import home, projects_view, sobre_view, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects_view, name='projects'),
    path('sobre/', sobre_view, name='sobre'),
    path('contato/', contact_view, name='contact')
]