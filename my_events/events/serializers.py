from rest_framework import serializers
from .models import *

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =EventCategory
        fields = ['id', 'event_category']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model =Event
        fields = ['id', 'event', 'event_timeInPT', 'event_timestamp', 'event_videoId','event_category']


class  TeamOrAthletSerializer(serializers.ModelSerializer):
    class Meta:
        model =TeamOrAthlet
        fields = ['id', 'teamOrAthlet','event_category']

class  CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields = ['id', 'timezone','location_state', 'user', 'event_category', 'teamOrAthlet', 'template_id']


class  ChoosenEventSerializer(serializers.ModelSerializer):
    class Meta:
        model =ChoosenEvent
        fields = ['id', 'reminder_note', 'customer', 'event']


class  CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields = ['id', 'content', 'event']


class  ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model =Reply
        fields = ['id','content','comment']






