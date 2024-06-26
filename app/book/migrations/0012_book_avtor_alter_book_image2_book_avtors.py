# Generated by Django 5.0.1 on 2024-05-20 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_book_file_book_file2_book_file3_book_file4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_avtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_block', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name_block2', models.CharField(max_length=255, verbose_name='Имя')),
                ('name_block3', models.CharField(max_length=255, verbose_name='Отчество')),
                ('active', models.BooleanField(default=True, verbose_name='Активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('template_name', models.CharField(blank=True, max_length=70, verbose_name='Выбор шаблона')),
            ],
            options={
                'verbose_name': 'Авторы книг',
                'verbose_name_plural': 'Авторы книг',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='prostopages', verbose_name='Картинка-2'),
        ),
        migrations.AddField(
            model_name='book',
            name='avtors',
            field=models.ManyToManyField(blank=True, related_name='avtor_book', to='book.book_avtor', verbose_name='Автор книги'),
        ),
    ]
