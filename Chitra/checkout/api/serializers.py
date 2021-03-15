from rest_framework import serializers
from posts.models import all_posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model: all_posts
        fields: ['post_name', 'description', 'image']