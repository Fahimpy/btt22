# Generated by Django 5.1.5 on 2025-01-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=150)),
                ('mobile_no', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('category', models.CharField(choices=[('Trainee', 'Trainee'), ('Trainer', 'Trainer')], max_length=10)),
            ],
        ),
    ]
