# Generated by Django 3.2.9 on 2021-12-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_profile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.CharField(default='0', max_length=15),
        ),
    ]
