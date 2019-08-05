from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # DOMAIN/pages/
    path('about/', views.about),  # DOMAIN/pages/about
    path('portfolio/', views.portfolio),  # D/pages/portfolio/
    path('help/', views.help),  # D/pages/help/
    path('cube/', views.cube),  # D/pages/cube
  #  path('check_int/', views.check_int),
   # path('pick_lotto/', views.pick_lotto),
]
