# Generated by Django 3.1.7 on 2021-12-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0009_auto_20211229_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_projects',
            name='project_Video_file',
            field=models.FileField(blank=True, null=True, upload_to='projects/video/'),
        ),
    ]
