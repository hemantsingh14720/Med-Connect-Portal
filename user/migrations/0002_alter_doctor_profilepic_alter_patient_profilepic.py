# Generated by Django 4.1.4 on 2023-02-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profilepic',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profilepic',
            field=models.FileField(upload_to=''),
        ),
    ]
