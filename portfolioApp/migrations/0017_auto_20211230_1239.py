# Generated by Django 3.1.7 on 2021-12-30 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0016_lead_contacts_generatedfrom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='lead_contact_numbers',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='our_work_Video',
        ),
    ]
