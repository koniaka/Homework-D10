from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView

from cars.models import Car


class CarsView(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        params = self.request.GET
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                # query.add(Q(**{key: value}), Q.AND)
                query &= Q(**{key: value})
        return {"cars": Car.objects.filter(query)}
