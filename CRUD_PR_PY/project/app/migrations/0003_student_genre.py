# Generated by Django 4.2.2 on 2023-06-19 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_student_email_student_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='genre',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
