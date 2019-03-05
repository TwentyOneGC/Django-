from django.db import models

# Create your models here.
class User(models.Model):
    gender = (                          #第一个参数是值，将被存储到数据库里。第二个值是在admin中下拉列表的显示。
        ('ban', '禁用'),
        ('activation', '激活'),
    )
    name = models.CharField(max_length=128, unique=True)    #unique 字段唯一 避免重复
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    statu = models.CharField(max_length=32, choices=gender, default='禁用')
    c_time = models.DateTimeField(auto_now_add=True)            #auto_now_add为添加时的时间，更新对象时不会有变动。
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'             #verbose_name的意思很简单，就是给你的模型类起一个更可读的名字一般定义为中文
        verbose_name_plural = '用户'  #这个选项是指定，模型的复数形式是什么，如果不指定Django会自动在模型名称后加一个’s’

class Store(models.Model):
    store_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = '商铺'
        verbose_name_plural = '商铺'


class OrderManage(models.Model):
    order_status = (
        (0, "制作"),
        (1, "测试"),
        (2, "退单"),
        (3, "完成"),
    )

    store_name = models.ForeignKey('Store', verbose_name="店铺名称", on_delete=models.CASCADE)
    order_num = models.CharField(max_length=128, unique=True, verbose_name="订单号")
    customer_ser = models.CharField(max_length=64, verbose_name="客服")
    author = models.CharField(max_length=64, verbose_name="作者")
    c_time = models.DateField(verbose_name="创建日期")
    o_detail = models.TextField(verbose_name="订单详情")
    status = models.SmallIntegerField(choices=order_status, default=0, verbose_name="订单状态")
    e_time = models.DateField( verbose_name="完成日期",null=True,blank=True)
    price = models.SmallIntegerField(default=0, verbose_name="订单金额")

    def __str__(self):
        return "({},{},{},{},{},{},{},{},{})".format(self.order_num, self.store_name, self.author, self.customer_ser, self.status, self.price, self.c_time, self.e_time,self.id)

    class Meta:
        verbose_name = '订单总表'
        verbose_name_plural = '订单总表'
        ordering = ['-c_time']