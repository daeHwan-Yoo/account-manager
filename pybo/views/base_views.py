from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    # http://localhost:8000/pybo/?page=1 처럼 GET방식으로 호출된 URL에서 page값을 가져올때 사용
    # http://localhost:8000/pybo/ 같이 페이지값 없이 호출된 경우, 디폴트로 1이라는 값 설정
    page = request.GET.get('page', '1')

    kw = request.GET.get('kw', '')  # 검색어

    # order_by: 조회 결과를 정렬하는 함수. order_by('-created_date')는
    # 역순으로 정렬하라는 것. -는 역방향, 없으면 순방향.
    question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            # subject__icontains=kw는 제목에 kw문자열이 포함되었는지를 의미
            # answer__author__username__icontains 는 답변을 작성한 사람의 이름에 포함되어 있는가
            # 란 의미
            # filter 함수에서 모델 속성 접근을 위해 __를 이용, 하위속성 접근 가능
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    # question_list는 게시물 전체를 의미하는 데이터, 10은 페이지당 보여줄 게시물 개수
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기

    # paginator 이용, 요청된 페이지에 해당하는 페이징 객체(page_obj)생성
    # 데이터 전체를 조회하지 않고 헤당 페이지의 데이터만 조회하도록 쿼리가 변경
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    # render 함수: 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
    # question_list 데이터를 pybo/question_list.html(템플릿) 파일에 적용,
    # html을 생성 후 리턴.
    # 템플릿 파일: 파이썬 데이터를 읽어서 사용할 수 있는 html 파일
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # 없는 데이터를 요청할 경우, 404 페이지를 리턴
    # pk는 Question 모델의 기본키
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)