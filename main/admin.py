from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from .models import *
from parler.admin import TranslatableAdmin
from django.utils.safestring import mark_safe

admin.site.register(Visit)
# Register your models here.

@admin.register(Banner)
class Banner(TranslatableAdmin):
    pass


@admin.register(Projects)
class Projects(TranslatableAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }


@admin.register(News)
class News(TranslatableAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }


@admin.register(SiteSettings)
class SiteSettings(TranslatableAdmin):
    pass


@admin.register(Tender)
class Tender(TranslatableAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }


@admin.register(Tables)
class Tables(TranslatableAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin, DraggableMPTTAdmin):
    mptt_level_indent = 50
    search_fields = ('translations__name',)
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )

    something.short_description = 'something nice'

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }

@admin.register(StaticContent)
class StaticContentAdmin(TranslatableAdmin):
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }



@admin.register(About)
class About(TranslatableAdmin):
    pass

@admin.register(Membership)
class Membership(TranslatableAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug',)
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }

@admin.register(File)
class File(admin.ModelAdmin):
    list_display = ('title', 'file')
    list_display_links =  ('file',)

@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'loc')
    list_display_links = ('id', 'loc')


admin.site.register(Gallery)
admin.site.register(Video)

