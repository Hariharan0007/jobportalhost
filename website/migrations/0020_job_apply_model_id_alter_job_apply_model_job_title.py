# Generated by Django 4.0.4 on 2022-05-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_job_apply_model_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply_model',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_apply_model',
            name='job_title',
            field=models.CharField(max_length=100),
        ),
    ]
