# Generated by Django 3.2.19 on 2023-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreenetLicence',
            fields=[
                ('freenet_licence_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_of_net', models.CharField(db_column='type of net', max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'freenet_licence',
                'managed': False,
            },
        ),
    ]
