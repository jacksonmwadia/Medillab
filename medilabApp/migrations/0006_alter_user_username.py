# Generated by Django 5.1.3 on 2024-11-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medilabApp', '0005_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
