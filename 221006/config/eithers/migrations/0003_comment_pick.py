# Generated by Django 3.1.7 on 2022-10-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eithers', '0002_auto_20221006_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pick',
            field=models.CharField(choices=[(1, 'RED'), (0, 'BLUE')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
