from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter
from tags.models import Tag
from django.db.models import Case, QuerySet, When
from .models import CV


class CVFilter(FilterSet):
    skills = ModelMultipleChoiceFilter(
        field_name='skills__name',
        lookup_expr='icontains',
        to_field_name='name',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = CV
        fields = ["skills"]
