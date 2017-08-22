from django.contrib import admin

from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    search_fields = ['room', 'first_name', 'last_name']
    list_display = ['room', 'full_name', 'date_range']
    list_filter = ['start_date', 'end_date']

    @staticmethod
    def full_name(obj):
        return f'{obj.first_name} {obj.last_name}'

    @staticmethod
    def date_range(obj):
        return f'Booked from {obj.start_date.strftime(u"%m/%d/%y - %I:%M %p")} ' \
               f'to {obj.end_date.strftime(u"%m/%d/%y - %I:%M %p")}'


admin.site.register(Reservation, ReservationAdmin)
