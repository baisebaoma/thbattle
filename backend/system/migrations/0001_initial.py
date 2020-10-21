# Generated by Django 3.0.3 on 2020-05-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(help_text='正文', verbose_name='正文')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='名称', max_length=20, verbose_name='名称')),
                ('description', models.TextField(help_text='描述', verbose_name='描述')),
                ('version', models.IntegerField(help_text='兼容客户端版本', verbose_name='兼容客户端版本')),
                ('url', models.CharField(help_text='服务器地址', max_length=200, verbose_name='服务器地址')),
                ('branch', models.CharField(help_text='Git 分支', max_length=20, verbose_name='Git 分支')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('key', models.SlugField(primary_key=True, serialize=False, verbose_name='键')),
                ('value', models.CharField(max_length=200, verbose_name='值')),
            ],
            options={
                'verbose_name': '全局设置',
                'verbose_name_plural': '全局设置',
            },
        ),
    ]