from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Question, Choice
import datetime

import json


def demoJson(request):
    data = {
        'name': 'Raghav',
        'location': 'India',
        'is_active': False,
        'count': 28,
        'vietnam': 'Xin chào Django',
        'list': ['question 1', 'question 2', 'question 3']
    }
    dump = json.dumps(data, ensure_ascii=False).encode('utf8')
    # return JsonResponse(data, safe=True, json_dumps_params={'ensure_ascii': False},
    #                     content_type="application/json; charset=utf-8",)
    return HttpResponse(dump, content_type="application/json; charset=utf-8", status=200,)


def createQuestion(request):
    # Django insert
    # question = Question.create(question_display='Where are you hi?', question_text='Where are you hi?', pub_date=datetime.datetime.now(),rating= 1, active=True, year_in_school=Question.YEAR_IN_SCHOOL_CHOICES[1])
    question = Question.objects.create_question(question_display='Where are you hi hi?', question_text='Where are you hi hi?', pub_date=datetime.datetime.now(), rating=1, active=True, year_in_school=Question.YEAR_IN_SCHOOL_CHOICES[1])
    # question.save()
    return HttpResponse(content_type="application/json; charset=utf-8",)


def renderPageViewHtml(request):
    list_question = Question.objects.get()
    choice_question = Question.YEAR_IN_SCHOOL_CHOICES
    print(choice_question)
    context = {
        'name': 'Nguyễn Văn Tý',
        'title': 'Developer',
        'is_active': False,
        'list_question': list_question,
        'choice_question': choice_question,
    }
    return render(request, 'polls/index.html', context, )
