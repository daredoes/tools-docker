import csv

from django import get_version
from django.views.generic import TemplateView, View, DetailView
from django.http import JsonResponse, HttpResponse
from .models import ItemModel
# Create your views here.


class GreetingsView(TemplateView):
    template_name = 'hello.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            items = ItemModel.objects.all()
            rows = [ItemModel.json_keys().keys()]
            for item in items:
                data = item.to_json()
                rows.append(data.values())
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="inventory.csv"'

            writer = csv.writer(response)
            writer.writerows(rows)

            return response
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_count'] = ItemModel.objects.all().count()
        return context


class ItemDetailView(DetailView):
    template_name = 'itemmodel_detail.html'

    model = ItemModel

class ItemJsonView(DetailView):
    model = ItemModel

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        output = obj.to_json()
        return JsonResponse(output)