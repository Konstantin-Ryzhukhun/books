# Generated by Django 5.0.1 on 2024-05-20 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_otzivbook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otziv',
            options={'ordering': ['created_at'], 'verbose_name': 'Отзывы о сайте', 'verbose_name_plural': 'Отзывы о сайте'},
        ),
        migrations.AlterModelOptions(
            name='otzivbook',
            options={'ordering': ['-id'], 'verbose_name': 'Отзыв на книгу', 'verbose_name_plural': 'Отзывы на книги'},
        ),
        migrations.CreateModel(
            name='BookFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('file', models.CharField(blank=True, max_length=255, null=True, verbose_name='Файл fb2')),
                ('file2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Файл epub')),
                ('file3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Файл RTF')),
                ('file4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Файл Mobi')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='travelvideo', to='book.book', verbose_name='Выбранная книга')),
            ],
            options={
                'verbose_name': 'Файл книги',
                'verbose_name_plural': 'Файл книги',
                'ordering': ['-created_at'],
            },
        ),
    ]
