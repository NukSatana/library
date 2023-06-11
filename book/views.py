from django.shortcuts import render
from django.views import generic

from .models import *

def index(request):
    context = {
        'category': Categories.objects.all(),
        'category_123': Categories.objects.all().last(),
        'category_151': Categories.objects.all().first(),
        'home_img': PhotoHome.objects.all(),
        'photo_students': PhotoStudents.objects.all(),
        'teacher': Teachers.objects.all()
    }
    return render(request, 'book/index.html', context)

class HomeView(generic.DetailView):
    model = Cards
    context_object_name = 'category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = Categories.objects.all()
        context['edu'] = Edu_Comp.objects.all()
        context['category_123'] = Categories.objects.all().last()
        context['category_151'] = Categories.objects.all().first()
        context['home_img'] = PhotoHome.objects.all(),
        context['photo_students'] = PhotoStudents.objects.all(),
        context['teacher'] = Teachers.objects.all()
        return context
    template_name = 'book/category_c.html'

class BookDetailView(generic.DetailView):
    model = Cards
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.all()
        context['edu'] = Edu_Comp.objects.all()
        context['category_123'] = Categories.objects.all().last()
        context['category_151'] = Categories.objects.all().first()
        return context
    template_name = 'book/profile.html'

class BookCompDetailView(generic.DetailView):
    model = Edu_Comp
    context_object_name = 'component'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_123'] = Categories.objects.all().last()
        context['category_151'] = Categories.objects.all().first()
        return context
    template_name = 'book/category.html'
