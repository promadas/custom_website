# Generated by Django 4.1.3 on 2023-01-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_jobsapply'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsapply',
            name='developer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
