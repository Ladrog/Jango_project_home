# Generated by Django 5.0.6 on 2024-06-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.tag', verbose_name='Теги'),
        ),
    ]
