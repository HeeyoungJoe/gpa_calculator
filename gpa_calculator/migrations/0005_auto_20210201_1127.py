# Generated by Django 3.1.5 on 2021-02-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpa_calculator', '0004_auto_20210129_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='desired_standard',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('MN', 'minor'), ('GN', 'general'), ('MJ', 'major')], max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='standard',
            field=models.FloatField(choices=[(3.7, '3.7'), (4.5, '4.5'), (4.3, '4.3')], null=True),
        ),
    ]
