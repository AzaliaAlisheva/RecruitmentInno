# Generated by Django 5.0.6 on 2024-07-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0013_user_remove_vacancies_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectvacancieswithspecialists',
            name='overlap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='connectvacancieswithspecialists',
            name='specmark',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]
