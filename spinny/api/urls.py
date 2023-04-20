from django.urls import path, include
from . import views
from rest_framework.authtoken import views as DRFviews

urlpatterns = [
    path('UpdateDestroy/<int:pk>',views.BoxView.as_view()),
    path('add', views.createBoxView.as_view()),
    path('list', views.BoxListView.as_view()),
    path('userList', views.UserListView.as_view()),
    path('user/<int:pk>', views.UserView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth', DRFviews.obtain_auth_token)
]
