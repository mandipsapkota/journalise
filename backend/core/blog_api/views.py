from rest_framework import generics
from blog.models import Post 
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView): #list and create 
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass 

class PostDetail(generics.RetrieveDestroyAPIView): # Retrieve and Destroy
    pass