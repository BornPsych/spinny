# Generated by Django 4.2 on 2023-04-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_box_breadth_alter_box_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='box',
            name='volume',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
