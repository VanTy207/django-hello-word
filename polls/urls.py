from django.template.defaulttags import url
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

VERSION_API = 'api/v1'
FILTER_QUESTION = f'{VERSION_API}/filter-questions'

urlpatterns = [
    path(f'{VERSION_API}/demo-json', views.demoJson, name='demoJson'),
    path(f'{VERSION_API}/get-all-question', views.getAllQuestion, name='getAllQuestion'),
    path(f'{VERSION_API}/get-detail-question/<slug>/', views.getDetailQuestion, name='getDetailQuestion'),
    # path('api/v1/filter-questions/<str:type_filter>', views.filterQuestion, name='filterQuestion'),
    re_path(r'^api/v1/filter-questions/?$', views.filterQuestion, name='filterQuestion'),
    # re_path(r'^api/v1/filter-questions/pagination/(?P<page>\w+)/(?P<page_size>\w+)/$', views.filterQuestionPagination, name='filterQuestionPagination'),
    path('render-page-view', views.renderPageViewHtml, name='renderPageViewHtml'),
    path(f'{VERSION_API}/create-question', csrf_exempt(views.createQuestion), name='createQuestion'),
    path('create-choice', views.createChoice, name='createChoice'),
]

# (?:(?P<type>\d+)(?P<value>\d+)(?P<rating>\d+)(?P<sort>\d+)(?P<page>\d+)(?P<page_size>\d+)/)

# http://127.0.0.1:8000/api/v1/filter-questions/pagination/0/11/

# http://127.0.0.1:8000/api/v1/filter-questions/pagination-param/?page=1&page_size=2