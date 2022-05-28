from typing import Optional, Dict

from polls.models import Question, QuestionSortField, SortType


def map_question(self: Question) -> Optional[Dict]:
    json_question = None
    if self is not None:
        json_question = {
            'id': self.id,
            'question_display': self.question_display,
            'question_text': self.question_text,
            'active': self.active,
            'rating': self.rating,
            'pub_date': self.pub_date
        }
    return json_question


def map_type_filter(self: str) -> Optional[QuestionSortField]:
    if self == '1':
        return QuestionSortField.NAME
    elif self == '2':
        return QuestionSortField.TIME
    elif self == '3':
        return QuestionSortField.RATING
    else:
        return QuestionSortField.NAME


def map_sort_type_filter(self: str) -> Optional[SortType]:
    if self == 'asc':
        return SortType.ASC
    elif self == 'desc':
        return SortType.DESC
    else:
        return SortType.ASC
