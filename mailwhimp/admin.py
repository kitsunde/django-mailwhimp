from django.contrib import admin
from mailwhimp.models import Campaign, List, Application


class ApplicationAdmin(admin.ModelAdmin):
    actions = ['load_lists']

    def load_lists(self, request, queryset):
        for application in queryset.all():
            application.load_lists()


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'list', 'send_time')

    actions = ['send_test']

    def send_test(self, request, queryset):
        for campaign in queryset.all():
            campaign.test_send([request.user.email])


admin.site.register(Application, ApplicationAdmin)
admin.site.register(List)
admin.site.register(Campaign, CampaignAdmin)