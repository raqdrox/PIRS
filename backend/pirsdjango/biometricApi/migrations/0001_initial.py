# Generated by Django 4.1.7 on 2023-04-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FingerprintIdMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fingerprint', models.TextField(blank=True)),
            ],
        ),
    ]
