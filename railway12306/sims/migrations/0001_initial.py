# Generated by Django 3.2.5 on 2021-12-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, db_column='PASSWORD', max_length=100, null=True)),
                ('jobnumber', models.CharField(blank=True, db_column='JOBNUMBER', max_length=100, null=True)),
                ('postision', models.CharField(blank=True, db_column='POSTISION', max_length=100, null=True)),
            ],
            options={
                'db_table': 'administrator',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Deleted',
            fields=[
                ('dingdanhao', models.CharField(db_column='DINGDANHAO', max_length=100, primary_key=True, serialize=False)),
                ('passengerid', models.CharField(blank=True, db_column='PASSENGERID', max_length=100, null=True)),
                ('deletetime', models.DateTimeField(db_column='DELETETIME')),
            ],
            options={
                'db_table': 'deleted',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, db_column='PASSWORD', max_length=100, null=True)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, db_column='AGE', null=True)),
                ('sex', models.CharField(blank=True, db_column='SEX', max_length=100, null=True)),
                ('idnumber', models.CharField(blank=True, db_column='IDNUMBER', max_length=100, null=True)),
                ('tel', models.CharField(blank=True, db_column='TEL', max_length=100, null=True)),
            ],
            options={
                'db_table': 'passenger',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('num', models.CharField(db_column='NUM', max_length=100, primary_key=True, serialize=False)),
                ('trainid', models.CharField(blank=True, db_column='TRAINID', max_length=100, null=True)),
                ('dapartureplace', models.CharField(blank=True, db_column='DAPARTUREPLACE', max_length=100, null=True)),
                ('arrivalplace', models.CharField(blank=True, db_column='ARRIVALPLACE', max_length=100, null=True)),
                ('daparturetime', models.CharField(blank=True, db_column='DAPARTURETIME', max_length=100, null=True)),
                ('arrivaltime', models.CharField(blank=True, db_column='ARRIVALTIME', max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, db_column='PRICE', null=True)),
                ('seattype', models.CharField(blank=True, db_column='SEATTYPE', max_length=100, null=True)),
                ('amount', models.IntegerField(blank=True, db_column='AMOUNT', null=True)),
            ],
            options={
                'db_table': 'ticket',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticketlist',
            fields=[
                ('dingdanhao', models.CharField(db_column='DINGDANHAO', max_length=100, primary_key=True, serialize=False)),
                ('passengerid', models.CharField(blank=True, db_column='PASSENGERID', max_length=100, null=True)),
                ('passengername', models.CharField(blank=True, db_column='PASSENGERNAME', max_length=100, null=True)),
                ('passengeridnum', models.CharField(blank=True, db_column='PASSENGERIDNUM', max_length=100, null=True)),
                ('trainid', models.CharField(blank=True, db_column='TRAINID', max_length=100, null=True)),
                ('dapartureplace', models.CharField(blank=True, db_column='DAPARTUREPLACE', max_length=100, null=True)),
                ('arrivalplace', models.CharField(blank=True, db_column='ARRIVALPLACE', max_length=100, null=True)),
                ('daparturetime', models.CharField(blank=True, db_column='DAPARTURETIME', max_length=100, null=True)),
                ('arrivaltime', models.CharField(blank=True, db_column='ARRIVALTIME', max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, db_column='PRICE', null=True)),
                ('seattype', models.CharField(blank=True, db_column='SEATTYPE', max_length=100, null=True)),
                ('createtime', models.DateTimeField(db_column='CREATETIME')),
            ],
            options={
                'db_table': 'ticketlist',
                'managed': True,
            },
        ),
    ]