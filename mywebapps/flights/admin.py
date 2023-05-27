from django.contrib import admin

from .models import Flight

#to see the proper table format

class FlightAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'client_id', 'client_name', 'client_email',
                      'batch', 'destination')

# Register your models here.

admin.site.register(Flight, FlightAdmin)
