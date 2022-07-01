from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('sign-up/', views.sign_up, name='sign_up'),
    # User
    path('user/', views.user_index, name='user_index'),
    path('personal/', views.personal, name='personal'),

    path('favourite/', views.favourite, name='favourite'),
    path('add-favourite/', views.add_favourite, name ='add_favourite'),
    path('editpersonal/', views.editPersonal, name ='editPersonal'),
    path('moveEditPersonal/', views.moveEditPersonal, name ='moveEditPersonal'),

    path('about/', views.about, name='about'),
    path('all-estates/', views.all_estates, name='all_estates'),
    
    path('product-detail/<int:id>/', views.product_detail, name='product_detail'),
    path('category-detail/<int:id>/', views.category_detail, name='category_detail'),
]
