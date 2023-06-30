from django import forms
from tour.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'photo']
        labels = {
            'subject': '제목',
            'content': '내용',
            'photo': '사진'
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {

            'content': '답변내용'
        }