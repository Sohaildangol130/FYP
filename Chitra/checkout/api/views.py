from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from posts.models import all_posts
from checkout.api.serializers import PostsSerializer

@api_view(['GET'])
def api_detail_checkout_view(request, slug):
    try:
        checkout = all_posts.objects.get(id=slug)
    except all_posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = all_posts(checkout)
        return Response(serializer.data)
