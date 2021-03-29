from django.urls import path, include
from rest_framework import routers

from .views import JournalEntryViewSet

router = routers.DefaultRouter()
router.register(r'entries', JournalEntryViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]