# Generated by Django 5.1.1 on 2024-11-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shope_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('contact_details', models.CharField(max_length=500, null=True)),
                ('pin', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]