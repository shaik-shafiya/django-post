# Generated by Django 4.2.3 on 2023-07-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shafi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
