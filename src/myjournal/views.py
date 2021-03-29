import csv

from django import get_version
from django.views.generic import TemplateView, View, DetailView
from django.http import JsonResponse, HttpResponse
from .models import JournalEntry
from .serializers import JournalEntrySerializer

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins


class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer