from django.urls import path, include
from . import views
from rest_framework.authtoken import views as DRFviews

urlpatterns = [
    path('update/<int:pk>',views.BoxUpdate.as_view()),
    path('add', views.createBoxView.as_view()),
    path('list', views.BoxListView.as_view()),
    path('userDataList', views.UserListView.as_view()),
    path('user/<int:pk>', views.UserView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth', DRFviews.obtain_auth_token),
    path('box/delete/<int:pk>', views.BoxDestroyView.as_view())
]
