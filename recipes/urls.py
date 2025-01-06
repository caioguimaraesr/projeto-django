from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), #/home
    path('recipes/<int:id>/', views.recipes, name="recipe"), #pagina de cada receita determinada pelo ID
]