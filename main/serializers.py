from rest_framework.serializers import ModelSerializer
from .models import Item, ItemImage, Order
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(ModelSerializer):
    discount_notifications = serializers.BooleanField(source='profile.discount_notifications')

    class Meta:
        model = User
        fields = ['username', 'email', 'discount_notifications']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        discount_notifications = profile_data.get('discount_notifications')

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile = instance.profile
        if discount_notifications is not None:
            profile.discount_notifications = discount_notifications
            profile.save()

        return instance

class ItemImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ItemImage
        fields = ['image', 'is_main']

    def get_image(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url

class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'