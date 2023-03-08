from django.contrib import admin

from admin_notif.models import CreateUser, ReviewLike


@admin.register(CreateUser)
class ResponseGetCreateUserAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user_id', 'username', 'email', 'status')
    search_fields = ('_id', 'user_id')
    empty_value_display = '-empty-'


@admin.register(ReviewLike)
class ResponseGetReviewLikeAdmin(admin.ModelAdmin):
    list_display = ('_id', 'review_id', 'username', 'email', 'status')
    search_fields = ('_id', 'user_id')
    empty_value_display = '-empty-'
