# Generated by Django 4.0.2 on 2022-02-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice',
            field=models.TextField(),
        ),
    ]
