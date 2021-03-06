# Generated by Django 3.1.7 on 2021-12-29 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0007_auto_20211124_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead_contacts',
            options={'verbose_name_plural': 'Lead Contact'},
        ),
        migrations.AddField(
            model_name='our_projects',
            name='project_Video_file',
            field=models.FileField(blank=True, null=True, upload_to='projects/video/', validators=[django.core.validators.FileExtensionValidator(['csv', 'docx', 'pdf'])]),
        ),
        migrations.AddField(
            model_name='our_projects',
            name='project_video_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='our_projects',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='our_projects',
            name='video_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='our_projects',
            name='video_heading',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
