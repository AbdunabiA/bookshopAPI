# Generated by Django 4.0.3 on 2022-04-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='usern', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
