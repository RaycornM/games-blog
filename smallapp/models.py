from django.db import models

# Create your models here.
#老师类
class Peoples(models.Model):
    username = models.CharField(max_length=50)#用户名
    password = models.CharField(max_length=30)#密码
    createtime = models.DateTimeField(auto_now_add=True)#日期类型（默认当前）
    sex = models.CharField(max_length=10)
    is_delete = models.IntegerField() #1代表正常状态 0删除状态 2冻结状态
    class Meta: # 设置表名
        db_table='Pro_Users'