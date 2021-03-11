from django.urls import path, include
from rest_framework import routers

from .views import ItemDetailView, GreetingsView, ItemJsonView, ItemModelViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemModelViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'<uuid:pk>/', ItemDetailView.as_view(), name='detail'),
    path(r'<uuid:pk>/json', ItemJsonView.as_view(), name='detail-json'),
]