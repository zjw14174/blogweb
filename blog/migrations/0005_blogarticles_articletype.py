# Generated by Django 2.1.4 on 2019-08-23 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190823_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticles',
            name='articletype',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogArticlesType', verbose_name='分类'),
        ),
    ]
