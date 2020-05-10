from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/like', views.post_like, name='post_like'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
    path('post/<int:pk>/unpublish', views.post_unpublish, name='post_unpublish'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('accounts/signup', views.signup, name='signup'),
    path('post/<int:pk>/comment_write2', views.comment_write2, name='comment_write2'),
    path('post/<int:pk>/comment_write2/<int:parent>', views.comment_write2, name='comment_write2'),
    path('post/<int:>/comment_remove/<int:commentpk>', views.comment_remove, name='comment_remove'),
    path('post/<int:>/comment_approve/<int:commentpk>', views.comment_approve, name='comment_approve'),
]
