from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from api.models import Event, Organization, User


class RegistrationSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'organization']
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def to_representation(self, obj):
        result = super(RegistrationSerializer, self).to_representation(obj)
        result.pop('password', None)
        return result

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'title', 'description', 'address', 'postcode')
        read_only_fields = ('id',)


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date')
        read_only_fields = ('id',)


class FullEventUserSerializer(RegistrationSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class FullEventOrganizationSerializer(serializers.ModelSerializer):
    members = FullEventUserSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('id', 'title', 'description', 'address', 'postcode', 'members')
        read_only_fields = ('id',)
    
    def to_representation(self, obj):
        result = super(FullEventOrganizationSerializer, self).to_representation(obj)
        address = result.pop('address', None)
        postcode = result.pop('postcode', None)
        result.update({'address_postcode': str(postcode) + ' ' + address})
        result.update({'members': result.pop('members', None)})
        return result
    

class FullEventSerializer(serializers.ModelSerializer):
    organizations = FullEventOrganizationSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'organizations')
        read_only_fields = ('id',)
