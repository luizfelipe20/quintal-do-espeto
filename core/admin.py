import datetime
from datetime import datetime, timezone, timedelta
from django.contrib import admin
from .models import Item, Order, ItemOrder, Table


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'values', 'created_at')
    search_fields = ('name',)

    def has_add_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_display = ('client', 'get_amount', 'created_at')
    inlines = [ItemOrderInline]
    readonly_fields=('created_by',)

    def get_amount(self, obj):
        return sum([elem.item.values * elem.amount for elem in obj.itemorder_set.all() if elem.item])
    get_amount.short_description = 'Total Pedido'

    def get_queryset(self, request): 
        if not request.user.is_superuser:
            now_utc = datetime.now(timezone.utc) - timedelta(hours=3)
            qs = super(OrderAdmin, self).get_queryset(request) 
            return qs.filter(created_by=request.user, created_at__date=now_utc)
        return super(OrderAdmin, self).get_queryset(request)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'availability')
    ordering = ('number',)
    def has_add_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True


admin.site.site_title = "Quintal do Espeto"
admin.site.site_header = "Quintal do Espeto"
admin.site.index_title = "Quintal do Espeto"