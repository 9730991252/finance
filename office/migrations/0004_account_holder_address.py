# Generated by Django 5.1.1 on 2024-12-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_remove_account_holder_account_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_holder',
            name='address',
            field=models.CharField(default='', max_length=1000),
        ),
    ]