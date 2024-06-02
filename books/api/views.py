from rest_framework.generics import GenericAPIView
from books.models import Book 
from books.api.serializers import BookSerializer
from rest_framework.mixins import   ListModelMixin,CreateModelMixin

class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)