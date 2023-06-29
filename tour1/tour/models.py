from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    # objects = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # 5장 - DB에서 칼럼에 null 값을 허용한다는 의미, blank=True는 작성 폼에서 form.is_valid() 검사시 값이 없어도 된다는 의미
    modify_date = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='tour/images/%Y/%m/%d/',
                              null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 외래키 제약조건 무시하고 연쇄 삭제됨
    # subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # 5장
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content

