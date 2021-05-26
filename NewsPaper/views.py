from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from django.utils.decorators import method_decorator

from .forms import NewsForm
from .models import Post, PostCategory
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


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(type='NE').order_by('-post_date_creation')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class NewsDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'single_news.html'  # название шаблона будет product.html
    context_object_name = 'single_news'  # название объекта. в нём будет
    queryset = Post.objects.filter(type='NE')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = PostCategory.objects.filter(post__id=self.kwargs.get('pk'))[0].category
        return context

@method_decorator(login_required, name='dispatch')
class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPaper.change_post',)
    template_name = 'news_create.html'
    form_class = NewsForm


# дженерик для редактирования объекта
@method_decorator(login_required, name='dispatch')
class NewsUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm
    permission_required = ('NewsPaper.add_post',)
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


@method_decorator(login_required, name='dispatch')
class NewsDelete(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'single_news'
