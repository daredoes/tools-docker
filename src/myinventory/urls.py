from django.urls import path

from .views import ItemDetailView, GreetingsView, ItemJsonView


urlpatterns = [
    path(r'', GreetingsView.as_view()),
    path(r'<uuid:pk>/', ItemDetailView.as_view(), name='detail'),
    path(r'<uuid:pk>/json', ItemJsonView.as_view(), name='detail-json'),
]