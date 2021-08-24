from core.models import *
from rest_framework import viewsets, permissions
from .serializers import *

#Board Viewset
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BoardSerializer