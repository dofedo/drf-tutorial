from rest_framework import serializers
from snippets.models import Snippet as SnippetModel

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetModel
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
