# Generated by Django 4.2 on 2023-04-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_box_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='breadth',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='box',
            name='height',
            field=models.FloatField(default=1),
        ),
    ]