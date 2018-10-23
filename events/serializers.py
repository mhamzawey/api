from events.models import Event
from rest_framework import serializers



class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150)
    description = serializers.CharField()
    category = serializers.CharField(max_length=80)
    start_date = serializers.DateField(format="%Y-%m-%d")# %I:%m:%s.%f")
    end_date = serializers.DateField(format="%Y-%m-%d")# %I:%m:%s.%f")
    link = serializers.URLField(max_length=128)
    web_source = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Event
        fields = ('id','title', 'description','category','start_date','end_date','link','web_source','created_at','updated_at')

