# Generated by Django 3.2.9 on 2021-12-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_phone_num_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(choices=[('Bhojpur', 'Bhojpur'), ('Dhankuta', 'Dhankuta'), ('Ilam', 'Ilam')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]