# Generated by Django 3.2.3 on 2021-06-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='short',
            old_name='name',
            new_name='initurl',
        ),
        migrations.AddField(
            model_name='short',
            name='shortenurl',
            field=models.CharField(default='', max_length=50),
        ),
    ]