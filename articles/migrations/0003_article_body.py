# Generated by Django 4.2 on 2025-04-10 05:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(default='No content yet'),
            preserve_default=False,
        ),
    ]
