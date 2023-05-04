from django.urls import path

from .views import (
    home_view, post_add, edit_post, delete_post
) 


urlpatterns = [
    # Accounts url
    path('', home_view, name='acceuil'),
    path('add_item/', post_add, name='add_item'),
    path('item/<int:pk>/edit/', edit_post, name='edit_post'),
    path('item/<int:pk>/delete/', delete_post, name='delete_post'),

]