# Generated by Django 4.2.4 on 2023-08-09 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0008_answer_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
