from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>',views.UserView.as_view()),
    path('create/user', views.createUserView.as_view()),
    # path('<int:pk>', views.model_view)
]
