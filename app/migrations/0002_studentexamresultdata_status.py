# Generated by Django 5.1.1 on 2024-10-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexamresultdata',
            name='status',
            field=models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail')], max_length=30, null=True),
        ),
    ]
