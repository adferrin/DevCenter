from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profiles_index, name='index'),
    path('profiles/create', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
    path('profiles/<int:pk>/update', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete', views.ProfileDelete.as_view(), name='profiles_delete'),
    path('profiles/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
    path('articles/', views.articles_index, name='articles_index'),
    path('articles/<int:article_id>/', views.articles_detail, name='articles_detail'),
    path('articles/create', views.ArticleCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/update/', views.ArticleUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', views.ArticleDelete.as_view(), name='articles_delete'),
    # path('articles/<int:article_id>/article_add_photo/', views.article_add_photo, name='article_add_photo'),
    path('github/', views.github, name='github'),
    path('twitter/', views.twitter, name='twitter'),
    path('accounts/signup/', views.signup, name='signup'),
]