from django.contrib import admin
from .models import UserProfile, Item, Order, ItemImage

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1
    fields = ['image', 'is_main']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'slug']
    inlines = [ItemImageInline]

admin.site.register(UserProfile)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)