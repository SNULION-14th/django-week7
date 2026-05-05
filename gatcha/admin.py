from django.contrib import admin
from .models import User, GatchaType, GatchaItemList, GatchaPoolItem, UserGatchaRecord, UserItemList

admin.site.register(User)
admin.site.register(GatchaType)
admin.site.register(GatchaItemList)
admin.site.register(GatchaPoolItem)
admin.site.register(UserGatchaRecord)
admin.site.register(UserItemList)
