from django.urls import path
from social_appe.views import Postlist,PostDetailView,PostEditView,PostDeleteView,CommentDeleteView

urlpatterns = [
    path('',Postlist.as_view(),name='post_list'),
    path('post/<int:pk>',PostDetailView.as_view(),name="post_details"),
    path('post/edit/<int:pk>',PostEditView.as_view(),name='post_edit'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>',CommentDeleteView.as_view(),name='comment_delete')
]