from django.urls import path
from rest_framework.schemas import get_schema_view

from foods import views

urlpatterns = [
    path("foods/", views.FoodList.as_view()),
    path("foods/<int:pk>/", views.FoodDetail.as_view()),
    path('openapi', get_schema_view(
        title="FridgeLog",
        description="API for fridgelog"
    ), name='openapi-schema'),
    # path('admin/', admin.site.urls),
]
