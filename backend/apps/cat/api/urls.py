from rest_framework.routers import DefaultRouter

from apps.cat.api import views

cat_router = DefaultRouter()
cat_router.register(r'cat/cat', views.CatViewSet, basename='cat')
cat_router.register(r'cat/food', views.FoodViewSet, basename='food')
