# Generated by Django 5.1.3 on 2024-11-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medilabApp', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user1', max_length=150),
            preserve_default=False,
        ),
    ]
