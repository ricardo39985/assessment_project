from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_item, name='create'),
    path('delete/<int:pk>/', views.delete_item, name='delete'),
    path('add', views.add_item, name='add')

]
