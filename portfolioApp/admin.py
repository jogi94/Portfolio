from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
def approvePost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Published'
		post.save()
approvePost.short_description = 'Approve Selected'


def draftPost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Draft'
		post.save()
draftPost.short_description = 'Draft Selected'

#
@admin.register(messageModel)
class messageModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('title', 'messageFor', 'message', 'created', 'status', )
	list_filter = ('status', )
	actions = [approvePost, draftPost,]

#
@admin.register(siteSetting)
class siteSettingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('title', 'siteDescription', 'created', 'status', )
	list_filter = ('status', )
	actions = [approvePost, draftPost,]

#
@admin.register(portifolio_page)
class portifolio_pageAdmin(ImportExportModelAdmin, SummernoteModelAdmin, admin.ModelAdmin):
	summernote_fields = ('about_content','performance_content', )
	list_display = ('our_name', 'our_profession', 'created', 'status', )
	list_filter = ('status', )
	actions = [approvePost, draftPost,]

#
@admin.register(educational_skills)
class educational_skillsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('heading', 'subtitle', 'created', 'status', )
	list_filter = ('status', )
	search_fields = ['heading', 'subtitle',]
	actions = [approvePost, draftPost,]

#
@admin.register(our_clients)
class our_clientsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('client_name', 'client_logo', 'created', 'status', )
	list_filter = ('status', )
	search_fields = ['client_name',]
	actions = [approvePost, draftPost,]

#ourProjects
class VideoAdmin(admin.StackedInline):
    model = videos

#
@admin.register(our_projects)
class our_projectsAdmin(ImportExportModelAdmin,SummernoteModelAdmin,  admin.ModelAdmin):
	summernote_fields = ('video_content', )
	list_display = ('project_name', 'project_subtitle', 'slug', 'created', 'status', )
	list_filter = ('status', )
	search_fields = ['project_name',]
	prepopulated_fields = {'slug': ('project_name',)}
	actions = [approvePost, draftPost,]
	inlines = [VideoAdmin]

@admin.register(videos)
class videosAdmin(admin.ModelAdmin):
    pass

#
@admin.register(lead_contacts)
class lead_contactsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('phone_number', 'name', 'generatedFrom', 'address', 'message', 'created', 'status', )
	list_filter = ('status', )
	search_fields = ['name', 'phone_number',]
	actions = [approvePost, draftPost,]