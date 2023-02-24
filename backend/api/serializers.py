from rest_framework import serializers
from account.models import Images
from account.models import User


class ImagesSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.serial")
    # def create(self, validated_data):
    # user_hobby = validated_data.pop('user_hobby')
    # profile_instance = Profile.objects.create(**validated_data)
    # for hobby in user_hobby:
    #     Hobby.objects.create(user=profile_instance,**hobby)
    # return profile_instance
    # user=serializers.PrimaryKeyRelatedField(read_only=True,default=)
    class Meta:
        model = Images
        exclude = ['user']

    # def save(self):
    #     user=User.objects.get(serial=self.context['request'].user)
    #     title = self.validated_data['title']
    #     article = self.validated_data['article']

    # def create(self, validated_data):
    #     print('%'*100)
    #     serial = validated_data.pop('user')
    #     print('&'*100)
    #     print(user)
    #     user = User.objects.get(serial=serial)
    #     return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('melli', 'serial', 'first_name', 'last_name',
                  'year_brithday', 'place', 'date_register', 'tel')
