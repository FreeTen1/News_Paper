from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.author_rating = self.objects


class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    state = 'ST'
    news = 'NE'

    FIELD = [
        (state, 'Статья'),
        (news, 'Новость')
    ]
    type = models.CharField(max_length=2, choices=FIELD)

    post_date_creation = models.DateTimeField(auto_now_add=True)
    post_heading = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_text[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date_creation = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
