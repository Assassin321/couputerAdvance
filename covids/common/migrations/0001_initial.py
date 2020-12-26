# Generated by Django 3.0.5 on 2020-12-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allStates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='NY', max_length=50)),
                ('Update', models.CharField(default='1/1/1970', max_length=50)),
                ('confirmed', models.IntegerField(default=0)),
                ('death', models.IntegerField(default=0)),
                ('recovered', models.IntegerField(default=0)),
                ('active', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
                ('updateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='timeSeriseConfirmed',
            fields=[
                ('uid', models.CharField(default='8000000', max_length=50, primary_key=True, serialize=False)),
                ('city', models.CharField(default='NYC', max_length=50)),
                ('province', models.CharField(default='NY', max_length=50)),
                ('cityName', models.CharField(default=None, max_length=50)),
                ('confirmed', models.CharField(default=None, max_length=5000)),
                ('Range', models.CharField(default=None, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='timeSeriseDeath',
            fields=[
                ('uid', models.CharField(default='8000000', max_length=50, primary_key=True, serialize=False)),
                ('city', models.CharField(default='NYC', max_length=50)),
                ('province', models.CharField(default='NY', max_length=50)),
                ('cityName', models.CharField(default=None, max_length=50)),
                ('death', models.CharField(default=None, max_length=5000)),
                ('Range', models.CharField(default=None, max_length=5000)),
            ],
        ),
    ]