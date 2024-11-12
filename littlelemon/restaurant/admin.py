from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    # Display specific fields in the list view in the Django admin
    list_display = ('name', 'price', 'category', 'description')
    # Add search functionality and filter options
    search_fields = ('name', 'category')
    list_filter = ('category',)

# Register the Menu model with custom admin settings
admin.site.register(Menu, MenuAdmin)
