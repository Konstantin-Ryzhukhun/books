# Generated by Django 5.0.1 on 2024-05-18 12:57

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_otziv_prostopages_book_image_book_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_block', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('text_block', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Картинка')),
                ('active', models.BooleanField(default=True, verbose_name='Активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('template_name', models.CharField(blank=True, help_text="Пример: 'book/prostopages.html'. Если не указано,  система будет использовать 'prostopages/prostopages.html'.", max_length=70, verbose_name='Выбор шаблона')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новость',
                'ordering': ['created_at'],
            },
        ),
    ]
