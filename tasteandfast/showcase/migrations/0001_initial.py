# Generated by Django 3.2.4 on 2021-06-21 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="section's name")),
                ('image', models.ImageField(upload_to='images/menu_sections')),
            ],
        ),
        migrations.CreateModel(
            name='Rubrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Rubric's name")),
                ('image', models.ImageField(upload_to='images/rubrics')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Rubric's name")),
                ('image', models.ImageField(upload_to='images/restaurants')),
                ('rubric_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.rubrics')),
            ],
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='dish name')),
                ('description', models.TextField(verbose_name='dish description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='dish price')),
                ('image', models.ImageField(upload_to='images/dishes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu_section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.menusections')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.restaurants')),
                ('rubric_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.rubrics')),
            ],
        ),
    ]
