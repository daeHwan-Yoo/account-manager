from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # form.cleaned_data.get는 폼의 입력값을 개별적으로 얻고 싶은 경우 사용
            # 인증시 사용할 사용자명과 비밀번호를 얻기 위해 사용
            username = form.cleaned_data.get('username')    
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증(username과 비밀번호 검증)
            login(request, user)  # 로그인(사용자 세션 생성)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})