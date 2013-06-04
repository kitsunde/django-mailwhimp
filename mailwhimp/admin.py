from django.contrib import admin
from mailwhimp.models import Campaign, List, Application


class ApplicationAdmin(admin.ModelAdmin):
    actions = ['load_lists']

    def load_lists(self, request, queryset):
        for application in queryset.all():
            application.load_lists()


admin.site.register(Application, ApplicationAdmin)
admin.site.register(List)
admin.site.register(Campaign)