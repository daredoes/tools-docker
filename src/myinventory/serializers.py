from rest_framework import serializers

from .models import ItemModel


class ItemModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemModel
        fields = ['url', 'name', 'description', 'image']