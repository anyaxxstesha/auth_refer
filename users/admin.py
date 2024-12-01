from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'invite_code', 'invited_by', 'is_superuser')
    list_filter = ('is_superuser',)
    search_fields = ('phone',)
