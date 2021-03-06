# Generated by Django 3.1.7 on 2021-11-24 08:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0005_auto_20211124_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Contact Form',
            },
        ),
    ]
