# Generated by Django 4.2 on 2023-07-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_test_campaign',
            fields=[
                ('test_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('test_city', models.CharField(max_length=100)),
                ('test_venue', models.CharField(max_length=100)),
                ('test_time', models.CharField(max_length=100)),
                ('test_date', models.CharField(max_length=100)),
                ('test_remark', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_test_campaign',
            },
        ),
    ]
