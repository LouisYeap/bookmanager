from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # django自动提供了主键id
    name = models.CharField(max_length=10)

    # 重写str方法显示书籍名字
    def __str__(self):
        return self.name


# 人物

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
