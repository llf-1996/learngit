from django.db import models

from tinymce.models import HTMLField


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, verbose_name="用户名称")
    password = models.CharField(max_length=50, verbose_name="用户密码")
    age = models.IntegerField(default=18, verbose_name="用户年龄")
    nickname = models.CharField(max_length=255, verbose_name="用户昵称")
    birthday = models.DateTimeField(auto_now_add=True, verbose_name="生日")
    # header = models.CharField(max_length=255, default="/static/img/default.png", verbose_name="用户头像")
    # header = models.FileField()
    header = models.ImageField(upload_to='static/img/headers/', default="static/img/default.png", verbose_name="用户头像")

    class Meta:
        ordering = ["id"]


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="文章标题")
    # content = models.TextField()
    content = HTMLField()
    publishTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255, null=True, blank=True, verbose_name="摘要")

    # 外键
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 级联删除，默认严格模式

    class Meta:
        ordering = ['-publishTime']
        # verbose_name = "文章"
        verbose_name_plural = "文章"


