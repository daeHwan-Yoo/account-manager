"""
관리자 화면
"""
from django.contrib import admin
from .models import Question

#question 모델에 세부 기능 추가할수 있는 클래스
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#question 모델을 관리자에 등록
admin.site.register(Question, QuestionAdmin)