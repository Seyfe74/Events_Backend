from django.urls import path
from events import views


urlpatterns =[ 
    path('events/', views.get_all_events),
    path('comments/', views.get_all_comments),
    path('categories/', views.get_all_categories),
    path('teamOrAthlet/', views.get_all_teamOrAthlet),
    path('choosenEvents/', views.add_choosenEvent),
    path('customer/', views.register_customer),
    path('', views.add_event),
    path('register', views.registration)
]