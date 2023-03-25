from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'location')
    
    def create(self, validated_data):
        profile = Profile.objects.create(
            bio=validated_data['bio'],
            location=validated_data['location']
        )
        return profile
    
    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
    