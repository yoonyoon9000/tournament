from django.urls import path
import main.views as views

urlpatterns = [
    path('', views.main, name="main"),
    path('apply/', views.apply, name="apply"),
    path('gameresult/', views.gameresult, name="gameresult"),
    path('mystatus/', views.mystatus, name="mystatus"),
]