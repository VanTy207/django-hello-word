from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

import json


def index(request):
    data = {
        'name': 'Raghav',
        'location': 'India',
        'is_active': False,
        'count': 28,
        'list': ['question 1', 'question 2', 'question 3']
    }
    dump = json.dumps(data)
    return HttpResponse(dump)


def renderPageViewHtml(request):
    list_question = Question.objects.all()
    choice_question = Question.YEAR_IN_SCHOOL_CHOICES
    print(choice_question)
    context = {
        'name': 'Nguyễn Văn Tý',
        'title': 'Developer',
        'is_active': False,
        'list_question': list_question,
        'choice_question': choice_question,
    }
    return render(request, 'polls/index.html', context)
