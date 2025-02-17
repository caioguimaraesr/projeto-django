from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), #/home
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<int:category_id>/', views.category, name='category'), 
    path('recipes/<int:id>/', views.recipes, name="recipe"), #pagina de cada receita determinada pelo ID
]