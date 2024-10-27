from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoe_list, name='shoe_list'),
    path('shoe/<int:pk>/', views.shoe_detail, name='shoe_detail'),
    path('shoe/create/', views.shoe_create, name='shoe_create'),
    path('shoe/update/<int:pk>/', views.shoe_update, name='shoe_update'),
]
