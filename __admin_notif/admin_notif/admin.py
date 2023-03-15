from django.contrib import admin

from admin_notif.models import AdminEvent, CreateUser, ReviewLike, User_obj


@admin.register(CreateUser)
class ResponseGetCreateUserAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user_id', 'username', 'email', 'status')
    search_fields = ('_id', 'user_id')
    empty_value_display = '-empty-'


@admin.register(ReviewLike)
class ResponseGetReviewLikeAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user_id', 'username', 'email', 'status', 'ready')
    search_fields = ('_id', 'user_id')
    empty_value_display = '-empty-'


@admin.register(AdminEvent)
class ResponseGetAdminEventAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user_ids', 'status', 'ready')
    empty_value_display = '-empty-'

# @admin.register(User_obj)
# class ResponseGetUser_objAdmin(admin.ModelAdmin):
#     list_display = ('_id',)
#     empty_value_display = '-empty-'
# admin.site.register(AdminEvent)
