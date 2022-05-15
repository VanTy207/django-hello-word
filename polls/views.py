import time

from django.shortcuts import render
from django.core.serializers.json import Serializer
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
import datetime
from typing import Optional, Dict

import json


def demoJson(request):
    data = {
        'result': 1,
        'message': 'success',
        'data': {
            'name': 'Raghav',
            'location': 'India',
            'is_active': False,
            'count': 28,
            'national': 'Xin chào Nguyễn Văn Tý',
            'list': ['question 1', 'question 2', 'question 3']
        },
    }
    return JsonResponse(data, safe=True, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8', status=200)


def map_create_question(question) -> Optional[Dict]:
    json_question = None
    if question is not None:
        json_question = {
            'question_display': question['questionDisplay'] if 'questionDisplay' in question else None,
            'question_text': question['questionText'] if 'questionText' in question else None,
            'pub_date': question['createDate'] if 'createDate' in question else datetime.datetime.now(),
            'active': question['active'] if 'active' in question else False,
            'rating': question['rating'] if 'rating' in question else 0,
        }
    return json_question


def createQuestion(request):
    data = {
        'result': 0,
        'message': 'error',
    }
    if request.method == 'POST':
        json_data = json.loads(request.body.decode("utf-8"))
        data_map = map_create_question(json_data)
        if data_map['question_display'] is not None and data_map['question_text']:
            _data: Optional[Question] = Question.objects.create_question(
                question_display=data_map['question_display'],
                question_text=data_map['question_text'],
                pub_date=data_map['pub_date'],
                rating=data_map['rating'],
                active=data_map['active'],
                year_in_school=Question.YEAR_IN_SCHOOL_CHOICES[1]
            )
            json_question = map_question(_data)
            data = {
                'result': 1,
                'message': 'success',
                'data': json_question
            }
        else:
            data = {
                'result': -1,
                'message': 'Field empty',
            }
    elif request.method == 'PUT':
        print('put')
    else:
        data = {
            'result': 0,
            'message': 'Error: create question',
        }
    return JsonResponse(data, content_type="application/json; charset=utf-8", status=200)


def getAllQuestion(request):
    data = {
        'result': 0,
        'message': 'error',
    }
    if request.method == 'GET':
        list_question = Question.objects.get_all_question()
        list_question_json = list(map(map_question, list_question))
        data = {
            'result': 1,
            'message': 'success',
            'data': list_question_json,
        }
    else:
        data = {
            'result': -1,
            'message': 'Not found',
            'data': []
        }
    return JsonResponse(data, safe=True, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8', status=200)


def getDetailQuestion(request, slug=None):
    data = {
        'result': 0,
        'message': 'error',
    }
    if request.method == 'GET':
        _data: Optional[Question] = Question.objects.get_question_detail(id=slug)
        json_question = map_question(_data)
        data = {
            'result': 1 if json_question is not None else -1,
            'message': 'success',
            'data': json_question
        }
    else:
        data = {
            'result': -1,
            'message': 'Not found',
            'data': []
        }
    return JsonResponse(data, safe=True, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8', status=200)


def map_question(question: Question) -> Optional[Dict]:
    json_question = None
    if question is not None:
        json_question = {
            'id': question.id,
            'question_display': question.question_display,
            'question_text': question.question_text,
            'active': question.active,
        }
    return json_question


def filterQuestion(request, slug=None):
    list_question = []
    data = {
        'result': 0,
        'message': 'error',
    }
    if request.method == 'GET':
        # print([Question.objects.get_question_detail(id=slug)])
        _data = [Question.objects.filter_question(active=slug)]
        data = {
            'result': 1,
            'message': 'success',
            'data': list_question,
        }
    else:
        data = {
            'result': -1,
            'message': 'Not found',
            'data': []
        }
    return JsonResponse(data, safe=True, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8', status=200)


def createChoice(request):
    choice = Choice.objects.create_choice(choice_text='Where are you hi hi?', votes=5, )
    return JsonResponse('choice', safe=True, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8', status=200)


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
