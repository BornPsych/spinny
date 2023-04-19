from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>',views.BoxView.as_view()),
    path('create', views.createBoxView.as_view()),
    path('', views.BoxListView.as_view()),
    # path('<int:pk>', views.model_view)
]
