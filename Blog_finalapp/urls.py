from django.urls import path
from . import views

urlpatterns = [
    path('display', views.B_post, name='display'),
    path('Blog', views.blog, name='Blog'),
    path('log', views.login, name='log'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('reg', views.register, name='reg'),
    path('blog', views.blog_display, name='blog'),
    path('update_blog/<int:id>', views.update, name='update_blog'),
    path('edit/<int:id>', views.edit_blog, name='edit'),
    path('like_post/<int:pk>', views.LikeView, name="like_post"),
    path('blog_detail/<int:pk>', views.BlogPostDetailView.as_view, name='blogpost_detail'),
    path('blog-detail/<int:id>', views.blogpost, name='blog-detail')
]