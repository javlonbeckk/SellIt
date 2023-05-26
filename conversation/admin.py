from django.contrib import admin

# local imports
from .models import Conversation, ConversationMessage

admin.site.register(Conversation)
admin.site.register(ConversationMessage)
