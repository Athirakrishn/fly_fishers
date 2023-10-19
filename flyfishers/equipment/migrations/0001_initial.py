# Generated by Django 3.2.19 on 2023-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('equipment_name', models.CharField(db_column='equipment name', max_length=45)),
                ('equipmentimage', models.CharField(max_length=500)),
                ('quandity', models.IntegerField()),
                ('subsidy', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'equipment',
                'managed': False,
            },
        ),
    ]
