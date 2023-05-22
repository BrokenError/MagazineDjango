# from django.contrib import admin
# from apps.orders.models import OrderItem, Order
#
#
# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'email', 'paid']
#
#     inlines = [OrderItemInline]
#
#
# admin.site.register(Order, OrderItem)
