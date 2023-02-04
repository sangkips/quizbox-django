from rest_framework import serializers

from .models import *


class TagSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Tag
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    title = serializers.CharField()
    body = serializers.CharField()

    class Meta:
        model = Question
        fields = ["id", "title", "body", "owner"]


class AnswerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Answer
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Vote
        fields = "__all__"
