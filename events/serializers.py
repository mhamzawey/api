from events.models import Event
from rest_framework import serializers



class EventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=225)
    category = serializers.CharField(max_length=80)
    start_date = serializers.CharField(max_length=80)
    end_date = serializers.CharField(max_length=80)
    link = serializers.URLField(max_length=128)


    class Meta:
        model = Event
        fields = ('id','title', 'description','category','start_date','end_date','link','created_at','updated_at')

