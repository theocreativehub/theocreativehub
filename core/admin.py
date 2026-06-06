from django.contrib import admin
from .models import Order, Portfolio, Comment, AdminReply

admin.site.register(Order)
admin.site.register(Portfolio)
admin.site.register(Comment)
admin.site.register(AdminReply)