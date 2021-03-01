from django.views.generic import \
    ListView, \
    DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(type='NE').order_by('-post_date_creation')


class NewsDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'single_news.html'  # название шаблона будет product.html
    context_object_name = 'single_news'  # название объекта. в нём будет
    queryset = Post.objects.filter(type='NE')
