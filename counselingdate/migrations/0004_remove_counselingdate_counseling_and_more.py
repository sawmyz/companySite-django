# Generated by Django 4.2.1 on 2023-07-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselingdate', '0003_counselingdate_counseling_alter_counselingdate_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counselingdate',
            name='counseling',
        ),
        migrations.AlterField(
            model_name='counselingdate',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]