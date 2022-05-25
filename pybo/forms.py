from django import forms
from pybo.models import Question, Answer

# QuestionForm은 모델 폼(forms.ModelForm)을 상속
# Question 모델과 연결된 폼, 속성으로 Question 모델의 subject와 content 사용
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        
        # 폼 위젯
        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        # 폼 레이블
        labels = {
            'subject': '제목',
            'content': '내용',
        }
# 답변 등록-장고 폼
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }