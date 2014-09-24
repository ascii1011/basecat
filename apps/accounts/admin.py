from django.contrib import admin

from .models import Account, Locale, ConnectionInformation

admin.site.register(Account)
admin.site.register(Locale)
admin.site.register(ConnectionInformation)

"""
from django.contrib.auth.admin import UserAdmin
#class ExpandedUserAdmin(admin.ModelAdmin):
class ExpandedUserAdmin(UserAdmin):
    fieldsets = [
        ('User Info', {'fields': ['username', 'first_name', 'last_name', 'email',
                                  'password', 'city', 'state', 
                                  'zip', 'website']}),
        ('Date information', {'fields': ['date_joined', 'last_login'], 'classes': ['collapse']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
    ]

    list_filter = ['is_staff', 'is_superuser', 'city']

    list_display = ['username', 'first_name', 'last_name', 'email', 'city', 'state',
                    'date_joined', 'last_login', 'is_active']
    
    add_fieldsets = (
        ("Auth", {
            "classes": ("wide",),
            "fields": ("email", "city", "password1", "password2")
            }
         ),
    )

admin.site.register(ExpandedUser, ExpandedUserAdmin)
"""