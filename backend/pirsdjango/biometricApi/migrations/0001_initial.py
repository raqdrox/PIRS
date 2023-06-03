# Generated by Django 4.1.7 on 2023-06-02 18:27

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
        migrations.CreateModel(
            name='PatientIdMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finger_id', models.IntegerField(unique=True)),
                ('patient_id', models.IntegerField(blank=True, default=-1)),
            ],
        ),
    ]
