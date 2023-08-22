from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.all_blogs, name='all_blogs'), #если больше ничего н е указано в запросе  "" то нужно отобразить страницы all_blogs
    path("<int:blog_id>/", views.detail, name='detail'),
]
