from rest_framework import serializers
from org_information.models import Organizations


class OrgDataSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Organizations
        fields = '__all__'
