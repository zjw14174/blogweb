# Generated by Django 2.1.4 on 2019-08-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogarticles_articletype'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticles',
            name='modifydate',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
    ]
