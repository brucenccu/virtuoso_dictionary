# Generated by Django 3.0.8 on 2020-07-23 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_word_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='name_type',
            new_name='pos',
        ),
    ]
