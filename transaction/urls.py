from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.TransectionAPI.as_view()),
    path('<str:str_1>/<int:num_1>/<int:num_2>/', views.TransectionAPI.as_view()),
    path('items/', views.ItemsAPI.as_view()),
    path('inventory/', views.InventoryAPI.as_view())

]

