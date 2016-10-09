from django.contrib import admin

from .models import NewMember, Group


class NewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'tel', 'email', 'college', 'dormitory', 'group', 'introduction')
    list_filter = ('sex','dormitory')
    fieldsets = (
        ('个人信息', {'fields': ('name', 'sex', 'college', 'dormitory')}),
        ('联系方式', {'fields': ('tel', 'email')}),
        ('分组意向&自我介绍', {'fields': ('group', 'introduction')}),
    )
    search_fields = ('name','tel')
    filter_horizontal = ()


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(NewMember, NewMemberAdmin)
admin.site.register(Group, GroupAdmin)

admin.site.site_header = '摄影协会报名后台'
admin.site.site_title = '摄影协会报名后台'
