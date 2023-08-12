from rest_framework import decorators, viewsets, filters
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

class PostView (viewsets.ModelViewSet) : 
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']