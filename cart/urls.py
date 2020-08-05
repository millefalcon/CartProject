from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.ItemCreate.as_view(), name='add_item'),
    path('list/', views.ItemView.as_view(), name='list_items'),
]