# Generated by Django 4.0.2 on 2022-06-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieTheater', '0004_alter_booking_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='ticket',
            field=models.ManyToManyField(blank=True, to='movieTheater.Ticket'),
        ),
    ]
