from django.contrib import admin
from .models import Event
from .models import EventCategory
from .models import TeamOrAthlet
from .models import Customer
from .models import ChoosenEvent
from .models import Comment
from .models import Reply






admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(TeamOrAthlet)
admin.site.register(Customer)
admin.site.register(ChoosenEvent)
admin.site.register(Comment)
admin.site.register(Reply)


