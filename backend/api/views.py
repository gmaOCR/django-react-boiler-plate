from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)
