# Generated by Django 3.1.4 on 2021-01-05 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20201228_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='club',
        ),
        migrations.AddField(
            model_name='member',
            name='nickname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Club',
        ),
    ]
