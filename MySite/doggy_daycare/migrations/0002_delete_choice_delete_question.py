# Generated by Django 4.2.4 on 2023-08-30 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doggy_daycare', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
