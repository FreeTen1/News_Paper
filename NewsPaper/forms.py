from django.forms import ModelForm
from .models import Post


class NewsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['type', 'post_heading', 'post_text', 'author', 'category']
