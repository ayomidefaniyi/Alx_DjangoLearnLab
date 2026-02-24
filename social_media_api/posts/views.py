from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get users the current user is following
        following_users = self.request.user.following.all()

        # Return posts from followed users ordered by newest first
        return Post.objects.filter(
            author__in=following_users
        ).order_by('-created_at')