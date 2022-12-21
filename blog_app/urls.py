from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )
from . import views

urlpatterns = [
    path('', views.mytest, name='portfolio-page'),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('downloads/', views.downloads, name='downloads-home'),
    path('about/', views.about, name='about_page'),
    path('mybio/', views.mybio, name='mybio-page'),
    
]
