"""itdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views


app_name = 'assets'
urlpatterns = [
    url(r'^index/', views.index,name='index'),
    url(r'^asset_query/', views.Asset_query.as_view(), name='asset_query'),
    url(r'^asset_query_json/all/$', views.Asset_query_all_json.as_view()),
    url(r'^asset_query_json/(?P<field_value>(.+))/$', views.Asset_query_json.as_view()),
]
