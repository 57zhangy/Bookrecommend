from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.EmailField()
    password=models.CharField(max_length=6,default='admin')
    u_img = models.ImageField(verbose_name="头像", upload_to='upload', default='upload/touxiang.jpg')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = "用户管理"


