from django.contrib import admin

from tickets.models import Order, Ticket


class TicketAdminInline(admin.StackedInline):
    model = Ticket


@admin.register(Order)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = [
        Order.profile.field.name,
        Order.datetime_order.field.name,
    ]
    inlines = [
        TicketAdminInline,
    ]
