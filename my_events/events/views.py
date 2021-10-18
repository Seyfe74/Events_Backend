from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_categories(request):
    categories = EventCategory.objects.all()
    serializer = EventCategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_teamOrAthlet(request):
    teamOrAthlet = TeamOrAthlet.objects.all()
    serializer = TeamOrAthletSerializer(teamOrAthlet, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def add_event(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request):
    if request.method == 'POST':
        #request.user
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save(user=request.data)
        #    serializer.save(user=request.user)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def register_customer(request):
    if request.method == 'POST':
        # request.user
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
        #    serializer.save(user=request.user)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        events = Customer.objects.all()
        serializer = CustomerSerializer(events, many=True)
        return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def add_choosenEvent(request):
    if request.method == 'POST':
        # request.user
        serializer = ChoosenEventSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
        #    serializer.save(user=request.user)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        events = ChoosenEvent.objects.all()
        serializer = ChoosenEventSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        events = Comment.objects.all()
        serializer = CommentSerializer(events, many=True)
        return Response(serializer.data)







