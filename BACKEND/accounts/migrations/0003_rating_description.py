# Generated by Django 5.0 on 2024-03-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rating_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
