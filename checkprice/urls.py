from django.urls import path

from . import views

urlpatterns = [
    path('checkprice/', views.search_item, name='search_item'),
]