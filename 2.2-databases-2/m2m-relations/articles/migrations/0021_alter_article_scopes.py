# Generated by Django 5.0.6 on 2024-07-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_alter_article_scopes_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag', verbose_name='Теги'),
        ),
    ]
