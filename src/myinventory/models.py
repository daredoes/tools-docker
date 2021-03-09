import uuid
from django.db import models
from collections import OrderedDict
import json


class ItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="items", blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def to_json(self):
        ret_val = self.json_keys()
        ret_val["id"] = str(self.id)
        ret_val["name"] = self.name
        ret_val["description"] = self.description
        try:
            ret_val["image"] = self.image.url
        except ValueError:
            pass  # There is no image

        return json.loads(json.dumps(ret_val))

    @staticmethod
    def json_keys():
        return {
            "id": "",
            "name": "",
            "description": "",
            "image": "",
        }

