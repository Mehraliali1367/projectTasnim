from rest_framework import serializers
from .models import Doctor, Presence, Visit, Services
from account.models import User


class DoctorSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.serial")

    class Meta:
        model = Doctor
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.serial")

    class Meta:
        model = Services
        fields = "__all__"


class PresenceSerializer(serializers.ModelSerializer):
    def get_more_doctor(self, obj):
        return {
            "name": obj.doctor.name,
            "id": obj.doctor.id
        }

    doctor = serializers.SerializerMethodField("get_more_doctor")

    class Meta:
        model = Presence
        fields = "__all__"


class VisitSerializer(serializers.ModelSerializer):
    def get_more_doctor(self, obj):
        return {
            "name": obj.doctor.name,
            "id": obj.doctor.id
        }

    def get_more_user(self, obj):
        return {
            "name": obj.user.full_name,
            "serial": obj.user.serial,
            "tel": obj.user.tel
        }

    doctor = serializers.SerializerMethodField("get_more_doctor")
    user = serializers.SerializerMethodField("get_more_user")

    class Meta:
        model = Visit
        fields = ('__all__')
