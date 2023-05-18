from posts.models import Comment, Group, Post
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'posts')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)
