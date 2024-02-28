from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # django自动提供了主键id
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # 在Django框架中，class Meta 是一个内部类，用于定义模型的一些元数据。这些元数据不会成为数据库表的一部分，但它们为Django的ORM（对象关系映射）层提供了关于如何与数据库交互的额外信息。
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'

    # 重写str方法显示书籍名字
    def __str__(self):
        return self.name


# 人物

class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1, '男'),
        (2, '女')
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=10, null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

