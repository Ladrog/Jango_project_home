# Generated by Django 5.0.6 on 2024-07-03 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_rename_name_tag_names_alter_article_scopes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='scope', through='articles.Scope', to='articles.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.tag', verbose_name='Тег'),
        ),
    ]
