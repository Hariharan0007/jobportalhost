# Generated by Django 3.2.13 on 2022-05-12 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_jobs_model_no_of_openings'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='jobs_model',
            unique_together={('job_title', 'job_company_name')},
        ),
    ]
