from django.contrib import admin

from .models import NewMember, Group1, Group2,Room


class NewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'tel', 'email', 'college', 'dormitory', 'group1','group2','room','introduction')
    list_filter = ('sex','dormitory','group1','group2','room')
    fieldsets = (
        ('个人信息', {'fields': ('name', 'sex', 'college', 'dormitory')}),
        ('联系方式', {'fields': ('tel', 'email')}),
        ('分组意向&自我介绍', {'fields': ('group1','group2','room', 'introduction')}),
    )
    search_fields = ('name','tel')
    filter_horizontal = ()


class Group1Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

class Group2Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(NewMember, NewMemberAdmin)
admin.site.register(Group1, Group1Admin)
admin.site.register(Group2, Group2Admin)
admin.site.register(Room, RoomAdmin)

admin.site.site_header = '摄影协会报名后台'
admin.site.site_title = '摄影协会报名后台'
