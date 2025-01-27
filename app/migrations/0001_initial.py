# Generated by Django 4.2 on 2023-06-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_account',
            fields=[
                ('acc_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('acc_name', models.CharField(max_length=100)),
                ('acc_district', models.CharField(max_length=100)),
                ('acc_place', models.CharField(max_length=100)),
                ('acc_category', models.CharField(max_length=100)),
                ('acc_phone', models.CharField(max_length=100)),
                ('acc_email', models.CharField(max_length=100)),
                ('acc_remark', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_account',
            },
        ),
    ]
