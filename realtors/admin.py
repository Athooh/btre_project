from django.contrib import admin
from .models import Realtor

# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp', 'hire_date')
    list_filter = ('name',)
    list_display_links = ('id', 'name')
    search_fields = ("name", "phone", "hire_date")
    #list_editable = ("is_mvp",)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
