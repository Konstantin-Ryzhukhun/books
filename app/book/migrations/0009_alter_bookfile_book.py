# Generated by Django 5.0.1 on 2024-05-20 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_otziv_options_alter_otzivbook_options_bookfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfile',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookfile', to='book.book', verbose_name='Выбранная книга'),
        ),
    ]