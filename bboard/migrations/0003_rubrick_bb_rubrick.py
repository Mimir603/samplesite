# Generated by Django 5.0.6 on 2024-06-18 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_alter_bb_options_alter_bb_content_alter_bb_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.AddField(
            model_name='bb',
            name='rubrick',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubrick', verbose_name='Рубрика'),
        ),
    ]
