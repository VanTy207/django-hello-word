from django.urls import path

from . import views

urlpatterns = [
    path('demo-json', views.demoJson, name='demoJson'),
    path('render-page-view', views.renderPageViewHtml, name='renderPageViewHtml'),
    path('create-question', views.createQuestion, name='createQuestion'),
]