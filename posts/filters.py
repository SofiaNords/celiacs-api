import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    score = django_filters.CharFilter(field_name='score', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['score']
