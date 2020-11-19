from django.db import models

# Create your models here.


# booktest_bookinfo
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20, db_column='title')  # db_column对于mysql数据库，因为btitle并不在mysql数据库里，所以才用db_column='title'来指定它原本对应的字段
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)  # IntegerField　　整形,参考链接：https://www.cnblogs.com/ellisonzhang/p/10679054.html
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
