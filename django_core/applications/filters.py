from django_filters import FilterSet, CharFilter

from django.db.models import Case, QuerySet, When
from .models import Application


class ApplicationFilter(FilterSet):
    class Meta:
        model = Application
        fields = ["project"]
