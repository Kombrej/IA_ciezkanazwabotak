# Generated by Django 5.0.6 on 2024-05-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkTime', '0005_staff_shiftendtime_staff_shiftstarttime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='ShiftEndTime',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
