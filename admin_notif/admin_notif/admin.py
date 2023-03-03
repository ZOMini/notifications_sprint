from django.contrib import admin

from admin_notif.models import CreateUser


@admin.register(CreateUser)
class ResponseGetCreateUserAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user_id', 'username', 'email', 'status')
    search_fields = ('_id', 'user_id')
    empty_value_display = '-empty-'
