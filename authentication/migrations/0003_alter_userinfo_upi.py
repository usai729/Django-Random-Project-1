# Generated by Django 4.2.1 on 2023-08-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_referredby_referredbyuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='UPI',
            field=models.BigIntegerField(),
        ),
    ]
