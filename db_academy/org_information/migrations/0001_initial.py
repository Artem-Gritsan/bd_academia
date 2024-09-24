# Generated by Django 5.1.1 on 2024-09-24 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=200, unique=True)),
                ('org_type', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200, null=True)),
                ('director', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('org_structure', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='org_information.organizations')),
            ],
            options={
                'db_table': 'organizations_2',
            },
        ),
    ]
