from django_filters import FilterSet, DateFilter
from .models import Post


# создаём фильтр
class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'post_date_creation': ['gte'],
            'post_heading': ['icontains'],
            'author__user__username': ['icontains'],
        }
