# Generated by Django 3.2.9 on 2021-12-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]