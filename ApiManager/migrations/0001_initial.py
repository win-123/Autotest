# Generated by Django 2.0.6 on 2018-09-28 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DebugTalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('debugtalk', models.TextField(default='#debugtalk.py', null=True)),
            ],
            options={
                'verbose_name': '驱动py文件',
                'db_table': 'DebugTalk',
            },
        ),
        migrations.CreateModel(
            name='EnvInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('env_name', models.CharField(max_length=40, unique=True)),
                ('base_url', models.CharField(max_length=40)),
                ('simple_desc', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '环境管理',
                'db_table': 'EnvInfo',
            },
        ),
        migrations.CreateModel(
            name='ModuleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('module_name', models.CharField(max_length=50, verbose_name='模块名称')),
                ('test_user', models.CharField(max_length=50, verbose_name='测试负责人')),
                ('simple_desc', models.CharField(max_length=100, null=True, verbose_name='简要描述')),
                ('other_desc', models.CharField(max_length=100, null=True, verbose_name='其他信息')),
            ],
            options={
                'verbose_name': '模块信息',
                'db_table': 'ModuleInfo',
            },
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('project_name', models.CharField(max_length=50, unique=True, verbose_name='项目名称')),
                ('responsible_name', models.CharField(max_length=20, verbose_name='负责人')),
                ('test_user', models.CharField(max_length=100, verbose_name='测试人员')),
                ('dev_user', models.CharField(max_length=100, verbose_name='开发人员')),
                ('publish_app', models.CharField(max_length=100, verbose_name='发布应用')),
                ('simple_desc', models.CharField(max_length=100, null=True, verbose_name='简要描述')),
                ('other_desc', models.CharField(max_length=100, null=True, verbose_name='其他信息')),
            ],
            options={
                'verbose_name': '项目信息',
                'db_table': 'ProjectInfo',
            },
        ),
        migrations.CreateModel(
            name='TestCaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('type', models.IntegerField(default=1, verbose_name='test/config')),
                ('name', models.CharField(max_length=50, verbose_name='用例/配置名称')),
                ('belong_project', models.CharField(max_length=50, verbose_name='所属项目')),
                ('include', models.CharField(max_length=500, null=True, verbose_name='前置config/test')),
                ('author', models.CharField(max_length=20, verbose_name='编写人员')),
                ('request', models.TextField(verbose_name='请求信息')),
                ('belong_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiManager.ModuleInfo')),
            ],
            options={
                'verbose_name': '用例信息',
                'db_table': 'TestCaseInfo',
            },
        ),
        migrations.CreateModel(
            name='TestReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('report_name', models.CharField(max_length=40)),
                ('start_at', models.CharField(max_length=40, null=True)),
                ('status', models.BooleanField()),
                ('testsRun', models.IntegerField()),
                ('successes', models.IntegerField()),
                ('reports', models.TextField()),
            ],
            options={
                'verbose_name': '测试报告',
                'db_table': 'TestReports',
            },
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('suite_name', models.CharField(max_length=100)),
                ('include', models.TextField()),
                ('belong_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiManager.ProjectInfo')),
            ],
            options={
                'verbose_name': '用例集合',
                'db_table': 'TestSuite',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('status', models.IntegerField(default=1, verbose_name='有效/无效')),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('type_name', models.CharField(max_length=20)),
                ('type_desc', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '用户类型',
                'db_table': 'UserType',
            },
        ),
        migrations.AddField(
            model_name='moduleinfo',
            name='belong_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiManager.ProjectInfo'),
        ),
        migrations.AddField(
            model_name='debugtalk',
            name='belong_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiManager.ProjectInfo'),
        ),
    ]
