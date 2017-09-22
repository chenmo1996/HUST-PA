from django.contrib import admin

from .models import NewMember, Group1, Group2,Room


class NewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'tel', 'qq','wechat', 'college', 'dormitory', 'room','guanli','group1','group2','introduction')
    list_filter = ('sex','dormitory','guanli','group1','group2','room')
    fieldsets = (
        ('个人信息', {'fields': ('name', 'sex', 'college', 'dormitory')}),
        ('联系方式', {'fields': ('tel', 'qq','wechat')}),
        ('分组意向&自我介绍', {'fields': ('room', 'guanli','group1','group2','introduction')}),
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

admin.site.site_header = 'kingstep报名后台'
admin.site.site_title = 'kingstep报名后台'
