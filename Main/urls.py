from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('load_data/', views.load_data, name='load_data'),
    path('teste/', views.teste, name='teste'),

]
