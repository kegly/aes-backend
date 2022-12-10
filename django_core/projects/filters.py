from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter
from tags.models import Tag
from .models import Project


class ProjectFilter(FilterSet):
    tags = ModelMultipleChoiceFilter(
        field_name='tags__name',
        lookup_expr='icontains',
        to_field_name='name',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Project
        fields = ["tags"]
