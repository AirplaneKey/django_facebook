"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


from facebook.views import play
from facebook.views import play2
from facebook.views import profile
from facebook.views import challenge
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import neww_feed
from facebook.views import edit_feed,remove_feed
# urlpatterns = [path() , path() , path()]
# urlpatterns = [첫번째 주소, 두번째 주소, 세번째 주소]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play2/', play2),
    path("LeeJaeHa/profile/", profile),
    path("challenge/", challenge),
    path("", newsfeed) , #  첫페이지
    path("feed/<pk>/", detail_feed) , #  자세히보기 페이지 보여줘
    path("feed/<pk>/edit/", edit_feed) , #  자세히보기 페이지 보여줘
    path("feed/<pk>/remove/", remove_feed) , #  자세히보기 페이지 보여줘
    path("new/", neww_feed), #path("new/", 글쓰기페이지 띄워줘)
]
