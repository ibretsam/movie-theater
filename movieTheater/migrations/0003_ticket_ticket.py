# Generated by Django 4.0.2 on 2022-06-28 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieTheater', '0002_remove_screening_ticket_screening_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket',
            field=models.CharField(default='Adult', max_length=20),
            preserve_default=False,
        ),
    ]