from django.urls import path

from .views import base_views, question_views, answer_views

"""
pybo/ 가 생략되는 이유는 이미 상위 파일인 config/urls.py에서 이미
매핑이 되었기에, pybo/ URL은 config/urls.py 파일에 매핑된
pybo/ 와 pybo/urls.py 파일에 매핑된 ''이 더해져 pybo/가 된다.
"""

# -pybo 앱 이외의 다른 앱이 프로젝트에 추가 될수 있음.
# -그렇다면 다른 앱에서 동일한 URL 별칭을 사용하게 될수 있음.
# -이를 방지하기 위해, 네임스페이스를 의미하는 app_name변수 지정.
# -URL 별칭도 수정할것
app_name='pybo'

urlpatterns = [
    # 링크의 주소 대신 별칭 사용: URL매핑에 name속성 부여
    # http://localhost:8000/pybo/ URL은 index라는 별칭 부여
    path('',
         base_views.index, name='index'),
    # 매핑 룰에 의해 pybo/2/는 pybo/<int:question_id>로 적용,
    # question_id에 2가 저장, views.detail 함수도 실행
    # http://localhost:8000/pybo/2와 같은 URL에는 detail 이라는 별칭 부여
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    # pybo:question_create에 해당되는 url 매핑 규칙
    # views.question_create 함수를 호출
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    #answer_create 별칭에 해당하는 url 매핑 규칙 등록
    # http://locahost:8000/pybo/answer/create/2/ 같은 페이지 요청하면
    # views.answer_create 함수 호출
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),

    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),

]