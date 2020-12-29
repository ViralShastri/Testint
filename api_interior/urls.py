from django.urls import path
from .views import interior_list ,article_detail,create_interior,login_list,create_user

urlpatterns = [

    path('interior/', interior_list),
    path('interior-create/',create_interior),
    path('detail/<int:pk>/', article_detail),
    path('login/',login_list),
    path('login-create/',create_user)
]