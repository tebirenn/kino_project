# Generated by Django 3.2.21 on 2023-09-07 13:46

from django.db import migrations, models
import django.db.models.deletion
import films.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True, upload_to=films.models.uniq_name_upload)),
                ('title_ru', models.CharField(max_length=255)),
                ('title_orig', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('prod_year', models.IntegerField()),
                ('timing', models.IntegerField()),
                ('premiere_date', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.country')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.genre')),
            ],
        ),
    ]
