# Generated by Django 5.0.6 on 2024-07-03 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_alter_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_article', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_tag', to='articles.tag', verbose_name='Тег'),
        ),
    ]
