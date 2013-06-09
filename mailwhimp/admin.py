from django.contrib import admin
from mailwhimp.models import Campaign, List, Application


class ApplicationAdmin(admin.ModelAdmin):
    actions = ['load_lists']

    def load_lists(self, request, queryset):
        for application in queryset.all():
            application.load_lists()


class ListAdmin(admin.ModelAdmin):
    actions = ['load_campaigns']

    def load_campaigns(self, request, queryset):
        for mailchimp_list in queryset.all():
            mailchimp_list.load_campaigns()


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'list', 'send_time')

    actions = ['send_test']

    def send_test(self, request, queryset):
        for campaign in queryset.all():
            campaign.test_send([request.user.email])


admin.site.register(Application, ApplicationAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Campaign, CampaignAdmin)