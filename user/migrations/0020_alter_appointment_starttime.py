# Generated by Django 4.1.4 on 2023-04-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_remove_appointment_dt_appointment_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='starttime',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
