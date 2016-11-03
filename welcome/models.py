#charset utf-8
from django.db import models


class Group1(models.Model):
    name = models.CharField(verbose_name='报名活动', max_length=64, null=True)
    description = models.TextField(verbose_name='报名活动', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '报名活动'
        verbose_name_plural = '报名活动'

# Group.objects.create(name="WeizhongTu", description="24")

class Group2(models.Model):
    name = models.CharField(verbose_name='报名项目', max_length=64,null=True)
    description = models.TextField(verbose_name='报名项目', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '报名项目'
        verbose_name_plural = '报名项目'

class Room(models.Model):
    name = models.CharField(verbose_name='是否摄协', max_length=64,null=True)
    description = models.TextField(verbose_name='是否摄协', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '是否摄协'
        verbose_name_plural = '是否摄协'

class NewMember(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    sex = models.IntegerField(verbose_name='性别', choices=((1, '男'), (0, '女'),(2,'其他')))
    tel = models.CharField(verbose_name='电话', max_length=11)
    email = models.CharField(verbose_name='qq或微信', max_length=64)
    college = models.CharField(verbose_name='专业-年级', max_length=64)
    dormitory = models.CharField(verbose_name='寝室住址', max_length=64)
    group1 = models.ForeignKey(Group1, verbose_name='报名活动',null=True)
    group2 = models.ForeignKey(Group2, verbose_name='报名项目',null=True)    
    room = models.ForeignKey(Room, verbose_name='是否摄协',null=True)    
    introduction = models.TextField(verbose_name='备注')

    def __str__(self):
        return self.name

    @property
    def district(self):
        return self.dormitory

    class Meta:
        verbose_name = '报名者'
        verbose_name_plural = '报名者'
