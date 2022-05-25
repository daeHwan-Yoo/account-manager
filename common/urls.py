from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    #common 디렉터리에서 login.html 파일을 참조 가능
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),

    #common 디렉터리에서 logout.html 파일을 참조 가능
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #로그인 화면에서 회원가입 링크를 누르면 views.signup 함수가 실행
    path('signup/', views.signup, name='signup'),

]