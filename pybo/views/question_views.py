from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm # forms.py는 부모 디렉터리에 있으니.
from ..models import Question

# render 함수에 전달된 {'form': form} 은 템플릿에서 질문 등록시 사용할
# 폼 엘리먼트를 생성할 때 쓰임
@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        # request.Post에 담긴 subject, content값이
        # QuestionForm의 subject, content 속성에 자동으로 저장
        form = QuestionForm(request.POST)   # request.POST에는 화면에서 사용자기 입력한 내용 담김
        if form.is_valid(): # 폼이 유효하다면
            # form에 저장된 데이터로 Question 데이터 저장하기 위한 코드
            question = form.save(commit=False) # commit=False는 임시 저장(create_date 값이 아직 미지정)
            question.author = request.user  # author 속성에 로그인 계정 저장            q
            question.create_date = timezone.now()   # 실체 저장을 위해 작성일시 설정
            question.save()     # 데이터를 실제로 저장
            return redirect('pybo:index')
    else:    # GET 요청방식, "질문 등록하기" 버튼을 클릭, question_create 함수 실행
        form = QuestionForm()   # QustionForm을 인수 없이 생성
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

# 질문 수정
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author: # request.user와 question.author이 다를경우
        messages.error(request, '수정권한이 없습니다') # messages 모듈 이용
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        # 질문수정 화면에 조회된 질문의 제목과 내용이 반영될 수 있도록 함
        # 속성 값이 instance로 채워짐, 질문을 수정하는 화면에서 제목과 내용이 채워진체로 보임
        # 수정된 내용 반영하는 케이스, 객체를 생성해야 함
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

# 질문 삭제
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

# 추천("좋아요")
@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다') # 본인 추천 방지
    else:
        question.voter.add(request.user)    # 여러 사람을 추가할 수 있음
    return redirect('pybo:detail', question_id=question.id)