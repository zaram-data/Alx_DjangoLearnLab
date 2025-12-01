from django.urls import path
from . import views  # import the entire views module

urlpatterns = [
    # Authentication / user views
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Blog post views (CRUD)
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

