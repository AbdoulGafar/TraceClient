from django.contrib import admin
from .models import ClientInfo

class ClientInfoAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'latitude', 'longitude', 'fingerprint', 'created_at')
    search_fields = ('client_id', 'fingerprint')

admin.site.register(ClientInfo, ClientInfoAdmin)
