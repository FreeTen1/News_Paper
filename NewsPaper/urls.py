from django.urls import path
from .views import NewsList, NewsDetail, SearchNews

urlpatterns = [
    path('search', SearchNews.as_view()),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
]