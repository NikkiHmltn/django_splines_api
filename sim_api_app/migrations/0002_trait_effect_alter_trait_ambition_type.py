# Generated by Django 4.2.7 on 2023-11-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trait',
            name='effect',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trait',
            name='ambition_type',
            field=models.CharField(blank=True, null=True),
        ),
    ]
