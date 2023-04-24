from rest_framework import serializers
from .models import Patient,MedicalData,EmergencyContact#,FingerprintData



class MedicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalData
        fields = ('id', 'blood_group', 'diseases','allergies','height','weight')

    def create(self, validated_data):
        medical_data = MedicalData.objects.create(
            blood_group=validated_data['blood_group'],
            diseases=validated_data['diseases'],
            allergies=validated_data['allergies'],
            height=validated_data['height'],
            weight=validated_data['weight']
        )
        return medical_data

    def update(self, instance, validated_data):
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        instance.diseases = validated_data.get('diseases', instance.diseases)
        instance.allergies = validated_data.get('allergies', instance.allergies)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance
    
class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = ('id', 'name', 'phone')

    def create(self, validated_data):
        emergency_contact = EmergencyContact.objects.create(
            name=validated_data['name'],
            phone=validated_data['phone']
        )
        return emergency_contact

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
'''    
class FingerprintDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerprintData
        fields = ('id', 'fingerprint_data')

    def create(self, validated_data):
        fingerprint_data = FingerprintData.objects.create(
            fingerprint_data=validated_data['fingerprint_data']
        )
        return fingerprint_data

    def update(self, instance, validated_data):
        instance.fingerprint_data = validated_data.get('fingerprint_data', instance.fingerprint_data)
        instance.save()
        return instance
'''
    
class PatientSerializer(serializers.ModelSerializer):
    medical_data = MedicalDataSerializer(partial=True)
    emergency_contact = EmergencyContactSerializer(partial=True)
    #fingerprint_data = FingerprintDataSerializer(partial=True)
    class Meta:
        model = Patient
        fields = ('id', 'name', 'dob','age', 'gender', 'phone', 'email', 'address','last_updated_time','last_updated_by', 'medical_data', 'emergency_contact')#, 'fingerprint_data')
    
    def create(self, validated_data):
        patient= Patient.objects.create(
            id=validated_data['id'],
            name=validated_data['name'],
            dob=validated_data['dob'],
            gender=validated_data['gender'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            address=validated_data['address'],
            last_updated_time=validated_data['last_updated_time'],
            last_updated_by=validated_data['last_updated_by'],
        )
        return patient
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.gender= validated_data.get('gender',instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.last_updated_time = validated_data.get('last_updated_time', instance.last_updated_time)
        instance.last_updated_by = validated_data.get('last_updated_by', instance.last_updated_by)
        
        if 'medical_data' in validated_data:
            medical = validated_data.pop('medical_data')
            nested_medical_data_serializer = self.fields['medical_data']
            nested_medical_instance = instance.medical_data
            nested_medical_data_serializer.update(nested_medical_instance, medical)
        
        if 'emergency_contact' in validated_data:
            emergency = validated_data.pop('emergency_contact')
            nested_emergency_contact_serializer = self.fields['emergency_contact']
            nested_emergency_instance = instance.emergency_contact
            nested_emergency_contact_serializer.update(nested_emergency_instance, emergency)
        '''
        if 'fingerprint_data' in validated_data:
            fingerprint = validated_data.pop('fingerprint_data')
            nested_fingerprint_data_serializer = self.fields['fingerprint_data']
            nested_fingerprint_instance = instance.fingerprint_data
            nested_fingerprint_data_serializer.update(nested_fingerprint_instance, fingerprint)'''
        

        return super(PatientSerializer, self).update(instance, validated_data)


    
