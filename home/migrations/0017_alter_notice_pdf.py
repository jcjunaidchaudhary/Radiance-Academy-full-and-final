# Generated by Django 4.0.2 on 2022-03-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_notice_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='pdf',
            field=models.FileField(default='Not Availabe', upload_to='Notice/pdf'),
        ),
    ]
