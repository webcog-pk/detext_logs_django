from django.contrib import admin
from core.models import UserAccessLog
# Register your models here.



@admin.register(UserAccessLog)
class UserAccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'os', 'path', 'ip', 'timestamp')
    readonly_fields = ('user', 'os', 'path', 'ip', 'timestamp')
    list_filter = ('user','os', 'timestamp')
