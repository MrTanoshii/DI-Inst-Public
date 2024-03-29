# Generated by Django 4.1.7 on 2023-03-15 08:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("totallynotascamwebsite", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="released_date",
            field=models.DateField(
                default=datetime.datetime(2023, 3, 15, 12, 14, 58, 893990)
            ),
        ),
    ]
