# Generated by Django 2.1.7 on 2019-03-11 12:31

from django.db import migrations, models
import faker.providers.address
import faker.providers.company
import faker.providers.person


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default=faker.providers.person.Provider.name, max_length=255)),
                ('price', models.IntegerField(default=7)),
            ],
            options={
                'db_table': 'album',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=faker.providers.person.Provider.name, max_length=255)),
                ('publisher', models.CharField(default=faker.providers.company.Provider.company, max_length=255)),
                ('address', models.CharField(default=faker.providers.address.Provider.address, max_length=255)),
            ],
            options={
                'db_table': 'author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default=faker.providers.person.Provider.name, max_length=255)),
                ('unit_price', models.FloatField(default=0.99)),
            ],
            options={
                'db_table': 'track',
                'managed': False,
            },
        ),
    ]