# Generated by Django 3.0.3 on 2021-03-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('nations', models.TextField()),
                ('team', models.TextField()),
                ('city', models.TextField()),
            ],
        ),
    ]
