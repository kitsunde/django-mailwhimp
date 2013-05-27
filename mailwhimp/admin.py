from django.contrib import admin
from mailwhimp.models import Campaign, List, Application

admin.site.register(Application)
admin.site.register(List)
admin.site.register(Campaign)