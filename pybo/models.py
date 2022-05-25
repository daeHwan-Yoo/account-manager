"""
-모델을 이용해 데이터베이스를 처리
-보통 SQL 쿼리문을 이용하지만, 모델을 사용하면 SQL 쿼리문의 도움없이
데이터를 쉽게 처리할수 있음
"""
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    # user모델을 ForeignKey로 적용
    # on_delete=models.CASCADE-계정이 삭제되면 이 계정이 작성한 질문을 모두 삭제하라는 의미
    # author을 기준으로 할지, voter을 기준으로 할지 명확하지 않다는 오류 해결을 위해 related_name 사용
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    
    # 글자수의 길이가 제한된 텍스트는 CharField
    subject=models.CharField(max_length=200) #제목(최대 200자)

    #글자수 제한할수 없는 텍스트는 TextField
    content=models.TextField()  #내용

    # 날짜와 시간에 관계된 속성
    create_date=models.DateTimeField()  #작성일시
    
    # null=True는 DB에서 modify_date 칼럼에 null 허용한다는 의미
    # blank=True는 form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 된다는 의미
    # 수정일시는 수정된 경우에만 생성되는 데이터이기에 null-True, blank=True 함
    modify_date = models.DateTimeField(null=True, blank=True)

    # 추천인 추가
    voter = models.ManyToManyField(User, related_name='voter_question')
    # 한명이 여러 개 질문을 추천 가능="다대다(N:N) 관계를 의미하는 ManyToManyField 사용

    # id값 대신 제목을 표시할 수 있다.
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    # ForeignKey: 기존 모델을 속성으로 연결하는 것, 다른 모델과 연결하기 위함
    # on_delete=models.CASCADE는 이 답변과 연결된 질문이 삭제될 때 답변도
    # 함께 삭제 된다는 의미
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


