# Generated by Django 2.2.4 on 2020-04-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default='admin', max_length=6)),
                ('u_img', models.ImageField(default='upload/touxiang.jpg', upload_to='upload', verbose_name='头像')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
            },
        ),
    ]
