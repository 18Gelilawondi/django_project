# Generated by Django 5.0.1 on 2024-02-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savouge', '0002_company_info_remove_about_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_info',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
