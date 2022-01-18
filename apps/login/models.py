from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=30,null=False,default='')
    login_name = models.CharField(max_length=20,null=False,unique=True,default='')
    login_pwd = models.CharField(max_length=32,null=False,default='')
    login_salt = models.CharField(max_length=32,null=False,default='')
    status = models.IntegerField(null=False,default=1)
    updated_time = models.DateTimeField(null=False)
    created_time = models.DateTimeField(null=False)

    class Meta:
        managed = True
        app_label = "login"
        db_table = "User"
        verbose_name = "User"
        verbose_name_plural = "User"
