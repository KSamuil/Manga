from django.contrib import admin
from .models import Tag, Account, Content

admin.site.register(Tag)
admin.site.register(Account)
admin.site.register(Content)