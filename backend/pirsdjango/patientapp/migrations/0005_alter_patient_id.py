# Generated by Django 4.1.7 on 2023-03-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0004_alter_emergencycontact_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
