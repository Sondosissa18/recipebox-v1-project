"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from recipe import views
from django.contrib.auth.views import LogoutView

# from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path("", views.index, name="homepage"),
    path("recipes/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("addauthor/", views.add_author, name="add_author"),
    # path(
    #     "addauthor/",
    #     staff_member_required(views.add_author),
    #     name="add_author",
    # ),
    path("addrecipe/", views.add_recipe, name="add_recipe"),
    path("login/", views.login_view, name="login"),
    # path("logout/", views.logout_view, name="logout"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
]
