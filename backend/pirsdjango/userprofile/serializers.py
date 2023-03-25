from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'location')
    
    def create(self, validated_data):
        profile = Profile.objects.create(
            name=validated_data['name'],
            location=validated_data['location']
        )
        return profile
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
    