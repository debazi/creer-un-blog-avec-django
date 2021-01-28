from . import views
from django.conf.urls import url

urlpatterns = [
   url(r'^$', views.PostList.as_view(), name='home'),
   url('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
