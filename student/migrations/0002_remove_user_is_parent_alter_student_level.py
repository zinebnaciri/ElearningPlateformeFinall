# Generated by Django 4.2 on 2023-05-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_parent',
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('Licence', 'Licence'), ('Master', 'Master')], max_length=25, null=True),
        ),
    ]
