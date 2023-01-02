from django.utils import timezone
from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"

    def validate_expiration_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("消費期限切れです")
        return value
