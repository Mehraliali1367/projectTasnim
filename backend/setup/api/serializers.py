from rest_framework import serializers
from account.models import Images
from account.models import User


class ImagesSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.serial")
    class Meta:
        model = Images
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('serial', 'melli', 'full_name', 'brithday', 'place', 'tel')
