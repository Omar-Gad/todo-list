from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = models.Todo
        fields = '__all__'



