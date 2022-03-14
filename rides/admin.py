from django.contrib import admin
from .models import *
# Register your models here.

# gi tilgang til å endre i adminpanel
admin.site.register(Ride)
admin.site.register(Station)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderTicket)
