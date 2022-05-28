from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional, List
from enum import Enum
from django.core.paginator import Paginator


class QuestionSortField(Enum):
    TIME = 1
    NAME = 2
    RATING = 3


class SortType(Enum):
    ASC = 1
    DESC = 2


class QuestionManager(models.Manager):
    def create_question(self, question_text, pub_date, rating, question_display, active, year_in_school):
        question = self.create(question_display=question_display, question_text=question_text, pub_date=pub_date, rating=rating, active=active, year_in_school=year_in_school)
        return question

    def get_all_question(self) -> List['Question']:
        list_question = self.all()
        print(len(list_question))
        return list_question

    def get_question_detail(self, id: int) -> Optional['Question']:
        try:
            return self.get(id=id)
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")

    def filter_question(self, type_sort: QuestionSortField, sort: SortType, value: str or None, rating: int or None, month: str or None, page: int, page_size: int = 10) -> List['Question']:
        print('type_sort ', type_sort)
        print('sort ', sort)
        print('value ', value)
        print('rating ', rating)
        print('page ', page)
        print('month ', month)

        list_question: List['Question'] = []
        request = Q()

        if type_sort == QuestionSortField.TIME:
            if month is not None:
                if value is not None:
                    request |= Q(pub_date__month=month)
                    queryValue = Q(question_display__startswith=value) or Q(question_text__startswith=value)
                    list_question = self.filter(queryValue, request).order_by('pub_date')
                else:
                    list_question = self.filter(Q(pub_date__month=month)).order_by('pub_date')
            else:
                list_question = self.all().order_by('-pub_date')

        elif type_sort == QuestionSortField.RATING:
            if rating is not None:
                if value is not None:
                    request |= Q(rating=rating)
                    queryValue = Q(question_display__startswith=value) or Q(question_text__startswith=value)
                    if sort == SortType.ASC:
                        list_question = self.filter(queryValue, request).order_by('id')
                    elif sort == SortType.DESC:
                        list_question = self.filter(queryValue, request).order_by('-id')
                else:
                    if sort == SortType.ASC:
                        list_question = self.filter(Q(rating=rating),).order_by('id')
                    elif sort == SortType.DESC:
                        list_question = self.filter(Q(rating=rating)).order_by('-id')
            else:
                if sort == SortType.ASC:
                    list_question = self.all().order_by('rating', 'id')
                elif sort == SortType.DESC:
                    list_question = self.all().order_by('-rating', '-id')

        else:
            if value is not None:
                request |= Q(question_display__startswith=value) or Q(question_text__startswith=value)
                list_question = self.filter(request)
            else:
                list_question = self.all().order_by('id')

        return list_question[(page * page_size):((page * page_size) + page_size)]


class ChoiceManager(models.Manager):
    def create_choice(self, choice_text, votes, ):
        choice = self.create(choice_text=choice_text, votes=votes)
        return choice


class Question(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    question_text = models.CharField(max_length=200, )
    pub_date = models.DateTimeField('date published')
    rating = models.IntegerField(default=0)
    question_display = models.TextField(max_length=255, null=True)
    active = models.BooleanField(default=False)
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='FR',
    )

    objects = QuestionManager()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    objects = ChoiceManager()

    @classmethod
    def create(cls, choice_text, votes):
        question = cls(choice_text=choice_text, votes=votes, )
        return question

    def __str__(self):
        return self.choice_text
