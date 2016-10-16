#charset utf-8
from django.db import models


class Group1(models.Model):
    name = models.CharField(verbose_name='第一志愿', max_length=64, null=True)
    description = models.TextField(verbose_name='第一志愿', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '管理层第一志愿报名'
        verbose_name_plural = '管理层第一志愿报名'

# Group.objects.create(name="WeizhongTu", description="24")

class Group2(models.Model):
    name = models.CharField(verbose_name='第二志愿', max_length=64,null=True)
    description = models.TextField(verbose_name='第二志愿', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '管理层第二志愿报名'
        verbose_name_plural = '管理层第二志愿报名'

class Room(models.Model):
    name = models.CharField(verbose_name='电影自习室', max_length=64,null=True)
    description = models.TextField(verbose_name='电影自习室', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影自习室'
        verbose_name_plural = '电影自习室'

class NewMember(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    sex = models.IntegerField(verbose_name='性别', choices=((1, '男'), (0, '女'),(2,'其他')))
    tel = models.CharField(verbose_name='电话', max_length=11)
    email = models.CharField(verbose_name='qq或微信', max_length=64)
    college = models.CharField(verbose_name='专业-年级', max_length=64)
    dormitory = models.CharField(verbose_name='寝室住址', max_length=64)
    group1 = models.ForeignKey(Group1, verbose_name='第一志愿',null=True)
    group2 = models.ForeignKey(Group2, verbose_name='第二志愿',null=True)    
    room = models.ForeignKey(Room, verbose_name='电影自习室',null=True)    
    introduction = models.TextField(verbose_name='备注')

    def __str__(self):
        return self.name

    @property
    def district(self):
        return self.dormitory

    class Meta:
        verbose_name = '报名者'
        verbose_name_plural = '报名者'
