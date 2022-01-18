from django.db import models

# Create your models here.

# 数据库类型
class Faculty(models.Model):
    name = models.CharField(verbose_name="数据库类型",max_length=100,unique=True,null=False)

    class Meta:
        managed = True
        app_label = "basicweb"
        db_table = "Basic_Faculty"
        verbose_name = "Faculty"
        verbose_name_plural = "Faculty"

    def __str__(self):
        return '%s' % self.name

# 数据库列表
class Major(models.Model):
    name = models.CharField(verbose_name="IP地址",max_length=100,unique=True,null=False)
    faculty = models.ForeignKey(verbose_name="所属类型",to=Faculty,on_delete=models.PROTECT)

    class Meta:
        managed = True
        app_label = "basicweb"
        db_table = "Basic_Major"
        verbose_name = "Major"
        verbose_name_plural = "Major"

    def __str__(self):
        return '%s' % self.name