# Generated by Django 2.2.5 on 2019-10-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stregsystem', '0009_auto_20191028_2057'),
        ('stregreport', '0004_remove_breadrazzia_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadrazzia',
            name='members',
            field=models.ManyToManyField(through='stregreport.RazziaEntry', to='stregsystem.Member'),
        ),
    ]