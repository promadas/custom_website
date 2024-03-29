# Generated by Django 4.1.3 on 2023-01-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('present_address', models.CharField(max_length=100)),
                ('university', models.CharField(blank=True, max_length=50, null=True)),
                ('resume', models.FileField(upload_to='nimusoft/resume/')),
                ('cover_letter', models.TextField()),
            ],
        ),
    ]
