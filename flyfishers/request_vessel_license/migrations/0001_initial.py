# Generated by Django 3.2.19 on 2023-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReqVesselLicense',
            fields=[
                ('req_vessel_license_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('vessel_no', models.IntegerField(db_column='vessel no')),
                ('request', models.CharField(max_length=45)),
                ('id_proof', models.CharField(db_column='id proof', max_length=45)),
                ('manifacture_date', models.DateField(db_column='manifacture date')),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'req_vessel_license',
                'managed': False,
            },
        ),
    ]
