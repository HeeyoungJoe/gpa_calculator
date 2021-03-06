# Generated by Django 3.1.5 on 2021-01-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpa_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='desired_standard',
            field=models.FloatField(choices=[('alt_2', 3.7), ('default', 4.5), ('alt_1', 4.3)], null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('MN', 'minor'), ('GN', 'general'), ('MJ', 'major')], max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='standard',
            field=models.FloatField(choices=[('alt_2', 3.7), ('default', 4.5), ('alt_1', 4.3)], null=True),
        ),
    ]
