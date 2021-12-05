from django.urls import path
from .views import home_view, ArticleDetailView, ProjectDetailView


urlpatterns = [
    path('', home_view, name="home"),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name="article-detail"),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name="project-detail"),
]