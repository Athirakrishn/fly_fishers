# Generated by Django 3.2.19 on 2023-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('u_id', models.IntegerField()),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]
