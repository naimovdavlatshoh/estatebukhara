from django.contrib import admin
from . models import *




class EstateAdmin(admin.ModelAdmin):
    list_display = ('title', 'rooms', 'square')

    
admin.site.register(Category)
admin.site.register(Estate, EstateAdmin)
admin.site.register(Gallery)
