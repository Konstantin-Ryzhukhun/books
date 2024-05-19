# Generated by Django 5.0.1 on 2024-05-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_block', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Картинка')),
                ('active', models.BooleanField(default=True, verbose_name='Активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('template_name', models.CharField(blank=True, help_text="Пример: 'book/prostopages.html'. Если не указано,  система будет использовать 'prostopages/prostopages.html'.", max_length=70, verbose_name='Выбор шаблона')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
                'ordering': ['created_at'],
            },
        ),
    ]