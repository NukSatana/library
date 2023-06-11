from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from book.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('component/<int:pk>/', BookCompDetailView.as_view(), name='comp-detail'),
    path('admin/', admin.site.urls, name='admin'),
    path('category/<int:pk>/', HomeView.as_view(), name='category')
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
