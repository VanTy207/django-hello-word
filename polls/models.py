from django.db import models

# Create your models here.
from django.db import models


class QuestionManager(models.Manager):
    def create_question(self, question_text, pub_date, rating, question_display, active, year_in_school):
        question = self.create(question_display=question_display, question_text=question_text,
                               pub_date=pub_date, rating=rating, active=active,
                               year_in_school=year_in_school)
        return question


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

    objects = QuestionManager

    @classmethod
    def create(cls, question_text, pub_date, rating, question_display, active, year_in_school):
        question = cls(question_display=question_display, question_text=question_text,
                       pub_date=pub_date, rating=rating, active=active,
                       year_in_school=year_in_school)
        return question

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
