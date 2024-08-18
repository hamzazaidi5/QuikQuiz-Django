# Generated by Django 4.2.4 on 2023-08-08 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_quiz_teacher_student_quizassignment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="quizassignment",
            options={"verbose_name": "Quiz_Assignments"},
        ),
        migrations.AlterModelOptions(
            name="student",
            options={"verbose_name": "Student_from_User"},
        ),
        migrations.AddField(
            model_name="quizassignment",
            name="questions",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="base.question",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=255),
        ),
    ]
