# Generated by Django 4.2.4 on 2023-08-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0018_classroom_quiz_students_classroomstudentenrolled_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="classroomstudentenrolled",
            name="enrolled",
            field=models.BooleanField(default=False),
        ),
    ]
