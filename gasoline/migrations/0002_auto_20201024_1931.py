# Generated by Django 3.1.2 on 2020-10-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasoline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='register',
            field=models.CharField(help_text='Unique Register given for the Mexican Govenment', max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='state',
            field=models.CharField(help_text='Official name of the Mexican state where is located the station', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='town',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
