from rest_framework import serializers
from products.models import Players


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ('id',
                  'name',
                  'nations',
                  'team',
                  'city')
