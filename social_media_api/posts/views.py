from rest_framework import viewsets, status, generics, permissions, filters
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from django_filters.rest_framework import DjangoFilterBackend  # ✅ import this
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions for safe methods
        if request.method in SAFE_METHODS:
            return True
        # Only the author can edit or delete
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # ✅ use this variable
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # create a notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
        return Response({"detail": "Post liked."}, status=status.HTTP_200_OK)


class UnlikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(post=post, user=request.user)
        if like.exists():
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)
