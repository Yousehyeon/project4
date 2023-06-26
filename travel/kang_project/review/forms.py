from django import forms

from review.models import Review, Answer


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'content']
        labels = {
            'subject': "제목",
            'content': "내용"
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '댓글내용'
        }