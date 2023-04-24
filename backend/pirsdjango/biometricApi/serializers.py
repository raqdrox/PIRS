from rest_framework import serializers
from .models import FingerprintIdMapping,PatientIdMapping

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
    

class PatientIdMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIdMapping
        fields = '__all__'

    def create(self, validated_data):
        patient_id_mapping = PatientIdMapping.objects.create(
            patient_id=validated_data['patient_id'],
            finger_id=validated_data['finger_id']
        )
        return patient_id_mapping
    



