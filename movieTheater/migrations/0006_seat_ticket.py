# Generated by Django 4.0.2 on 2022-06-29 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieTheater', '0005_alter_screening_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movieTheater.ticket'),
        ),
    ]