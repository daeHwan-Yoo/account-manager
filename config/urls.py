"""
페이지 요청이 발생하면 가장 먼저 호출되는 파일
URL 뷰 함수(views.py) 간의 매핑을 정의
예를 들면 pybo/ URL에 대한 매핑을 추가하는 것
"""

from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

#pybo/로 시작하는 페이지를 요청하면 pybo/urls.py파일의 매핑정보를 읽어서 처리함
urlpatterns = [
    path('admin/', admin.site.urls),
    
    #뒤에 '/' 붙인건 유저가 8000/pybo로 해도 8000/hybo/로 변환
    path('pybo/', include('pybo.urls')),

    # http://localhost:8000/common/ 으로 시작하는 URL은 common/urls.py 파일 참조
    path('common/', include('common.urls')),

    # '/' 에 해당되는 path
    path('', base_views.index, name='index'),

]
