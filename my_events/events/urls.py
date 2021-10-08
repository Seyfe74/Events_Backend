from django.urls import path
from events import views


urlpatterns =[ 
    path('all/', views.get_all_events),
    path('', views.add_event)
]