from django.db import models


# Create your models here.

class Students(models.Model):
    name = models.CharField("姓名", max_length=15, db_index=True)
    student_number = models.IntegerField("学号", unique=True, help_text="学号")
    age = models.IntegerField("年龄", help_text="年龄", db_index=True)
    cls = models.IntegerField("班级", help_text="班级")
    score = models.FloatField("分数", help_text="分数", default=0.0)
    remake = models.CharField("备注", help_text="备注", max_length=200)
    create_date = models.DateTimeField("创建时间", help_text="创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", help_text="更新时间", auto_now=True)

    class Meta:
        db_table = "students"
        ordering = ["id"]
