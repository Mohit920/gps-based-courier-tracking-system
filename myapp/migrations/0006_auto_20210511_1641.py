# Generated by Django 3.2.2 on 2021-05-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210511_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_order',
            name='cost',
            field=models.CharField(default='0.00', max_length=10),
        ),
        migrations.AlterField(
            model_name='new_order',
            name='id',
            field=models.CharField(default='IH6297H621', max_length=15, primary_key=True, serialize=False),
        ),
    ]
