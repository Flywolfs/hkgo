from django.urls import path

from . import views

urlpatterns = [
    path('checkprice/', views.search_item, name='search_item'),
    path('showrecords/',views.record_item, name='search_record')
]