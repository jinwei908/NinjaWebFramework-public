#from django.contrib.auth.models import User, Group
#from rest_framework import serializers
from restapi.models import *
from rest_framework_mongoengine import serializers

"""class UserSerializer(rest_framework.serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(rest_framework.serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')"""

class ToolSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tool
        fields = '__all__'
        
class InsertSerializer(serializers.DocumentSerializer):
    class Meta:
        model = InsertResult
        fields = '__all__'
        
class InsertRequestSerializer(serializers.DocumentSerializer):
    class Meta:
        model = InsertRequest
        fields = '__all__'
        
class DashboardDataSerializer(serializers.DocumentSerializer):
    class Meta:
        model = DashboardDataInstance
        fields = '__all__'
        