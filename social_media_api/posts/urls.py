from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedAPIView, LikePostAPIView, UnlikePostAPIView


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', FeedAPIView.as_view(), name='feed'),
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', LikePostAPIView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostAPIView.as_view(), name='unlike-post'),

]
