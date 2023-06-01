from django.urls import path
from .views import index,tampilanawal,grid,galeri
urlpatterns = [
    path('',index, name='index'),
    path('tampilanawal',tampilanawal, name='tampilanawal'),
    path('gridhtml',grid,name='grid'),
    path('galeri',galeri,name='galeri')
]
