from django.contrib import admin
from .models import Order, Portfolio, Comment, AdminReply


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_id', 'created_at')

    list_display = (
        'order_id',
        'client_name',
        'project_name',
        'status',
        'progress',
    )

    search_fields = (
        'order_id',
        'client_name',
        'project_name',
    )


admin.site.register(Portfolio)
admin.site.register(Comment)
admin.site.register(AdminReply)