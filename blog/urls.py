from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/post_new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
    path('post/<int:pk>/unpublish', views.post_unpublish, name='post_unpublish'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
]
