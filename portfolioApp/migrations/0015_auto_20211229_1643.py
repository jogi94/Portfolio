# Generated by Django 3.1.7 on 2021-12-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0014_auto_20211229_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='ourWork',
            new_name='our_work',
        ),
        migrations.AddField(
            model_name='videos',
            name='our_work_Video',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
