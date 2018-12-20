from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sunubusApp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('create', views.HeroesCreate)


urlpatterns = [
    path('listheroes/', views.HeroesList.as_view()),
    path('listheroes/<int:pk>/', views.HeroesDetail.as_view()),
    path('ligne/', views.LigneView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) #optionnal