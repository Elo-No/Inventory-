from rest_framework.serializers import ModelSerializer

from apps.account.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            ' first_name'
            ' last_name',
            'mobile_number',
            'role',
        )
