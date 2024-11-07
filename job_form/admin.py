from django.contrib import admin
from .models import Form
# Register your models here.


class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'occupation', 'created_at')
    search_fields = ('name', 'email', 'phone', 'occupation')
    list_filter = ('created_at',)
    # descending order (-)
    ordering = ('-name',)
    readonly_fields = ('created_at',)


admin.site.register(Form, FormAdmin)

