# Generated by Django 3.2.19 on 2023-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('vessel_id', models.AutoField(primary_key=True, serialize=False)),
                ('fishermen_id', models.IntegerField()),
                ('fishermen_name', models.CharField(db_column='fishermen name', max_length=45)),
                ('name_of_vessel', models.CharField(db_column='name of vessel', max_length=45)),
                ('register_no', models.IntegerField(db_column='register no')),
                ('license_no', models.IntegerField(db_column='license no')),
                ('crew', models.IntegerField()),
                ('year', models.IntegerField()),
                ('register_date', models.DateField(db_column='register date')),
                ('register_place', models.CharField(db_column='register place', max_length=45)),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'vessel',
                'managed': False,
            },
        ),
    ]