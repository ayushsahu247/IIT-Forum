from rest_framework import serializers
from posts.models import *
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"
