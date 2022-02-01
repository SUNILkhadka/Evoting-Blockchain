# Generated by Django 3.2.5 on 2021-11-20 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.candidate')),
            ],
        ),
    ]