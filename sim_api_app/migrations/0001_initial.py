# Generated by Django 4.2.7 on 2023-11-07 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimsPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('icon', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('E', 'Expansion'), ('G', 'Game'), ('S', 'Stuff'), ('K', 'Kit'), ('B', 'Base')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('icon', models.CharField(max_length=200)),
                ('description', models.CharField()),
                ('type', models.CharField(choices=[('AM', 'Ambition'), ('SK', 'Skill'), ('LT', 'Lot Trait'), ('LC', 'Lot Challenge'), ('ST', 'Sim Trait')], max_length=2)),
                ('ambition_type', models.CharField(null=True)),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim_api_app.simspack')),
            ],
        ),
    ]