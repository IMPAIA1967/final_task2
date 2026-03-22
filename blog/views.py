from rest_framework import viewsets
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .permissions import OwnerOnly, AuthorOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OwnerOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AuthorOnly]
