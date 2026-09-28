from django.contrib import admin
from .models import Project, Skill, Experience, Adventure, AdventurePhoto, Post, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'published', 'order')
    list_editable = ('featured', 'published', 'order')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'featured', 'order')
    list_filter = ('category',)
    list_editable = ('featured', 'order')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'current', 'order')
    list_editable = ('current', 'order')


class PhotoInline(admin.TabularInline):
    model = AdventurePhoto
    extra = 1


@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'featured', 'published', 'order')
    list_editable = ('featured', 'published', 'order')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]
    fieldsets = (
        ('Adventure', {'fields': ('title', 'slug', 'location', 'summary', 'story', 'cover_image')}),
        ('Instagram', {'fields': ('instagram_post_url', 'instagram_url')}),
        ('Display', {'fields': ('featured', 'published', 'order')}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published', 'order', 'updated_at')
    list_filter = ('category', 'published')
    list_editable = ('published', 'order')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')


admin.site.site_header = 'Suresh Shahi Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
