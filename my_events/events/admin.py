from django.contrib import admin
from .models import Event
from .models import EventCategory
from .models import Location
from .models import Customer
from .models import ChoosenEvent
from .models import Comment
from .models import Reply
from .models import TimeZone




admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(ChoosenEvent)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(TimeZone)

