from rest_framework import serializers

from .models import Poem, Favorite 

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'poem']
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)


class PoemModelSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model=Poem
        fields = ['id','title', 'author', 'poems', 'created_by']
        read_only_fields = ['created_at', 'updated_at', 'is_deleted']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['created_by'] = request.user  
        return super().create(validated_data)
    
class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Poem
        fields = ['id', 'poems']
        
