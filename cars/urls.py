from django.urls import path
from cars.views import CarsView

urlpatterns = [
    #path('search/', SearchResultsView.as_view(), name='search_results'),
    path('main/', CarsView.as_view(), name='car_list'),
]