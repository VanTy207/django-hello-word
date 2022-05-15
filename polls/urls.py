from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('api/v1/demo-json', views.demoJson, name='demoJson'),
    path('api/v1/get-all-question', views.getAllQuestion, name='getAllQuestion'),
    path('api/v1/get-detail-question/<slug>/', views.getDetailQuestion, name='getDetailQuestion'),
    path('api/v1/get-filter-question/<slug>/', views.filterQuestion, name='getDetailQuestion'),
    path('render-page-view', views.renderPageViewHtml, name='renderPageViewHtml'),
    path('api/v1/create-question', csrf_exempt(views.createQuestion), name='createQuestion'),
    path('create-choice', views.createChoice, name='createChoice'),
]