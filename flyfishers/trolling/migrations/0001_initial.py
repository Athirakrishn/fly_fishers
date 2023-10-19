# Generated by Django 3.2.19 on 2023-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trolling',
            fields=[
                ('trolling_id', models.AutoField(primary_key=True, serialize=False)),
                ('trolling_info', models.CharField(db_column='trolling info', max_length=200)),
                ('starting_date', models.DateField(db_column='starting date')),
                ('ending_date', models.DateField(db_column='ending date')),
            ],
            options={
                'db_table': 'trolling',
                'managed': False,
            },
        ),
    ]