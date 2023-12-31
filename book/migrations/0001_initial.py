# Generated by Django 4.2.2 on 2023-06-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_home', models.ImageField(upload_to='img_home')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_students', models.ImageField(upload_to='img_students')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachers', models.CharField(max_length=256)),
                ('position_o', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Edu_Comp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_edu_comp', models.CharField(max_length=200, unique=True)),
                ('cat_list', models.ManyToManyField(related_name='item', to='book.categories', verbose_name='Категории:')),
            ],
            options={
                'ordering': ['name_edu_comp'],
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='images_books')),
                ('file_downl', models.FileField(upload_to='file_books')),
                ('category', models.ManyToManyField(to='book.categories', verbose_name='Специальность')),
                ('edu_comp', models.ManyToManyField(related_name='books', to='book.edu_comp', verbose_name='Компоненты')),
            ],
        ),
    ]
