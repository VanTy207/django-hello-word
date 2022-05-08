from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('render-page-view', views.renderPageViewHtml, name='view'),
]