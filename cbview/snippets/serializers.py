from rest_framework import serializers
from snippets.models import Snippet as SnippetModel
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SnippetModel
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=SnippetModel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']