# Generated by Django 4.2.6 on 2023-10-12 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student Management System', 'verbose_name_plural': "Student Management System'"},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Contact',
            new_name='Age',
        ),
        migrations.AlterModelTable(
            name='student',
            table='',
        ),
    ]