# Generated by Django 4.0.4 on 2022-05-15 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_alter_job_apply_model_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job_apply_model',
            unique_together={('id', 'job_company_email')},
        ),
    ]
