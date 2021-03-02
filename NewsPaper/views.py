from django.views.generic import ListView, DetailView
from .models import Post
from .filters import NewsFilter


class SearchNews(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 1
    queryset = Post.objects.filter(type='NE').order_by('-post_date_creation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(type='NE').order_by('-post_date_creation')
    paginate_by = 5


class NewsDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'single_news.html'  # название шаблона будет product.html
    context_object_name = 'single_news'  # название объекта. в нём будет
    queryset = Post.objects.filter(type='NE')
