from rest_framework import serializers
from .models import FingerprintIdMapping

class FingerprintIdMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerprintIdMapping
        fields = '__all__'
    
    def create(self, validated_data):
        fingerprint_id_mapping = FingerprintIdMapping.objects.create(
            fingerprint=validated_data['fingerprint'],
        )
        return fingerprint_id_mapping
    
    def update(self, instance, validated_data):
        instance.fingerprint = validated_data.get('fingerprint', instance.fingerprint)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    



