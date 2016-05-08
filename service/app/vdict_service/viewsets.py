from rest_framework import viewsets, filters
from models import Word

from serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )
