from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'address', 'phone', 'email')
    
    def create(self, validated_data):
        profile = Profile.objects.create(
            name=validated_data['name'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            email=validated_data['email'],
        )
        return profile
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    