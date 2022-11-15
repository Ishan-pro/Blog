
from django.contrib import admin
from django.urls import path
from Posts.views import PostListView, SearchView, PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view()),
    path("search/", SearchView),
    path("view/<pk>", PostView.as_view())
]
