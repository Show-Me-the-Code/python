from django.contrib import admin
from messageboard.models import Message



class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name']}),
        ('context',{'fields':['context']}),
        ]
    list_display = ('name', 'context', 'vote_date')

admin.site.register(Message, MessageAdmin)
