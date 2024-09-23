from django.contrib import admin

from sinais.models import Historical, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "email",
    )


@admin.register(Historical)
class HistoricalAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "username",
        "email",
        "person",
    )
