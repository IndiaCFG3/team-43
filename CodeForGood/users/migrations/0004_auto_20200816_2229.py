# Generated by Django 3.0.6 on 2020-08-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200816_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='usertype',
            field=models.CharField(choices=[('admin', 'admin'), ('hr', 'hr')], default='admin', max_length=10),
        ),
    ]
