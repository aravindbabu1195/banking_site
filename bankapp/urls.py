from django.urls import path

from bankapp import views

app_name = 'bank'
urlpatterns = [

    path('', views.home, name='home'),
    

]
