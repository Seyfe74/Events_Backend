from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model =Event
        fields = ['id', 'event_category', 'time_zone', 'event_name']


class  ChoosenEventSerializer(serializers.ModelSerializer):
    class Meta:
        model =ChoosenEvent
        fields = ['id', 'customer_id', 'event_id']