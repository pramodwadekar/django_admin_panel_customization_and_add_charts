# Generated by Django 4.2.6 on 2023-10-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_options_rename_contact_student_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]