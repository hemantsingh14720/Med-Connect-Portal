# Generated by Django 4.1.4 on 2023-04-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_alter_appointment_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='starttime',
            field=models.DateTimeField(default='2023-04-29T16:03', null=True),
        ),
    ]
