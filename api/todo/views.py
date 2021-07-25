from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = (permissions.IsAuthenticated,) # only authenticated users have access to it.
    permission_classes = (permissions.DjangoModelPermissions,)
