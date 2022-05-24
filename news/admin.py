from django.contrib import admin
from news.forms import SocialSidebarForm

# Register your models here.
from news.models import *



@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    prepopulated_fields = {'url':('title',)}

admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    prepopulated_fields = {'url':('name',)}

admin.site.register(Category, CategoryAdmin)



class SocialSidebarAdmin(admin.ModelAdmin):
    form = SocialSidebarForm
    list_display = ['link_address', 'social_name']
    prepopulated_fields = {'social_name':('link_address',)}

    fieldsets = (
        (None, {
            'fields': ('link_address', 'social_name', 'icon', 'background')
            }),
        )

admin.site.register(SocialSidebar, SocialSidebarAdmin)