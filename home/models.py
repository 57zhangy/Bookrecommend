from django.db import models

# Create your models here.
class book(models.Model):
    no = models.CharField(max_length=50,blank=False,verbose_name="编码",default='')
    name = models.CharField(max_length=50,blank=False,verbose_name="书名",default='')
    price = models.CharField(max_length=50,blank=False, verbose_name="价格",default='')
    cover = models.ImageField(verbose_name="封面", upload_to='upload', default='img/default.png')
    url=models.URLField(verbose_name='URL',blank=True,default='')
    publish=models.CharField(verbose_name='出版社',max_length=50,default='',blank=True)
    rating=models.CharField(verbose_name='评分',max_length=5,default='0')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "图书管理"
        verbose_name_plural = "图书管理"

class hits(models.Model):
    userid=models.IntegerField(default=0)
    bookid=models.IntegerField(default=0)
    hitnum=models.IntegerField(default=0)

    def __str__(self):
        return str(self.userid)

    class Meta:
        verbose_name = "点击量"
        verbose_name_plural = "点击量"
