from django.urls import path
from . import views
app_name = 'form1'
urlpatterns = [
    path('', views.registration_view, name='registration'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('home/', views.home_view, name='home'),
]
