from django.urls import path
from .views import NewsList, NewsDetail, SearchNews, NewsCreate, NewsUpdate, NewsDelete, upgrade_me

urlpatterns = [
    path('search', SearchNews.as_view()),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('create', NewsCreate.as_view()),
    path('create/<int:pk>', NewsUpdate.as_view()),
    path('delete/<int:pk>', NewsDelete.as_view()),
    path('upgrade/', upgrade_me, name='upgrade'),
]