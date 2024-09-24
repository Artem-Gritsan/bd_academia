from rest_framework import serializers
from org_information.models import Organizations


class OrgDataSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Organizations
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.parent:
            representation['parent'] = {
                'id' : instance.parent.id,
                'org_name' : instance.parent.org_name,
                'org_type' : instance.parent.org_type
            }
        return representation
