# Generated by Django 4.2.4 on 2023-08-11 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0027_alter_question_answer_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="last_date",
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name="question",
            name="answer_options",
            field=models.CharField(
                choices=[
                    ("SHORT", "Short"),
                    ("MULTIPLE", "Multiple"),
                    ("TRUEFALSE", "TrueFalse"),
                ],
                default="Short",
                max_length=255,
            ),
        ),
    ]
