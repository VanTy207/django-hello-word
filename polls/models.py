from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional, List


class QuestionManager(models.Manager):
    def create_question(self, question_text, pub_date, rating, question_display, active, year_in_school):
        question = self.create(question_display=question_display, question_text=question_text, pub_date=pub_date, rating=rating, active=active, year_in_school=year_in_school)
        return question

    def get_all_question(self) -> List['Question']:
        list_question = self.all()
        return list_question

    def get_question_detail(self, id:int) -> Optional['Question']:
        try:
            return self.get(id=id)
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")

    def filter_question(self, active) -> List['Question']:
        return self.filter(active=True, question_display__startswith='What')

    def natural_key(self):
        return self.natural_key()


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

    @classmethod
    def create(cls, question_text, pub_date, rating, question_display, active, year_in_school):
        question = cls(question_display=question_display, question_text=question_text,
                       pub_date=pub_date, rating=rating, active=active,
                       year_in_school=year_in_school)
        return question

    def natural_key(self):
        return self.question_display, self.question_text, self.rating

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
