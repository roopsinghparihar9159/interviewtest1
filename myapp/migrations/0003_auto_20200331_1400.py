# Generated by Django 3.0.1 on 2020-03-31 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200319_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.CharField(max_length=3, null=True),
        ),
    ]