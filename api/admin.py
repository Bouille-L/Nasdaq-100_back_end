from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Columns to display
    list_filter = ('created_at',)  # Filters
    search_fields = ('name', 'email', 'message')  # Searchable fields

admin.site.register(ContactMessage, ContactMessageAdmin)
