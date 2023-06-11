from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name_category = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name_category

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

class Edu_Comp(models.Model):
    name_edu_comp = models.CharField(max_length=200, unique=True)
    cat_list = models.ManyToManyField(to=Categories, verbose_name='Категории:', related_name='item')

    class Meta:
        ordering = ['name_edu_comp']

    def __str__(self):
        return self.name_edu_comp

    def get_absolute_url(self):
        return reverse('comp-detail', kwargs={'pk': self.pk})

class Cards(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    img = models.ImageField(upload_to='images_books')
    file_downl = models.FileField(upload_to='file_books')
    category = models.ManyToManyField(to=Categories, verbose_name="Специальность", related_name='books_cat')
    edu_comp = models.ManyToManyField(to=Edu_Comp, verbose_name='Компоненты', related_name='books')
    def __str__(self):
        return f'Name: {self.title} | Category: {self.category.name} '

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

class Teachers(models.Model):
    teachers = models.CharField(max_length=256)
    position_o = models.CharField(max_length=256)

    def __str__(self):
        return f'Teachers: {self.teachers} - {self.position_o}'

class PhotoHome(models.Model):
    photo_home = models.ImageField(upload_to='img_home')


class PhotoStudents(models.Model):
    photo_students = models.ImageField(upload_to='img_students')

    def __str__(self):
        return f'Photo students: {self.photo_students}'
