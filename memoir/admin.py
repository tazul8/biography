from django.contrib import admin
from .models import Article, Banner, Contact, Education, Skill, Project, SocialMedia


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(Banner, BannerAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'image_tag')
admin.site.register(Article, ArticleAdmin)

admin.site.register(Education)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_name', 'percentage_of_expertise', 'title', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'image_tag')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')
admin.site.register(Contact, ContactAdmin)

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('social_media', 'social_media_url')


