# Generated by Django 4.2.16 on 2024-11-12 14:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testlar', '0003_alter_variant_savol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
