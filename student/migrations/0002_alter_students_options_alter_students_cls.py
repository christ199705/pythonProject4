# Generated by Django 4.0.4 on 2022-07-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='students',
            name='cls',
            field=models.IntegerField(help_text='班级', max_length=4, verbose_name='班级'),
        ),
    ]