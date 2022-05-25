import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# @register.filter 애너테이션 적용-템플릿에서 해당 함수를 필터로 사용가능
@register.filter
def sub(value, arg):
    return value - arg

# 마크다운 필터 작성
# markdown 모듈과 mark_safe 함수를 이용하여 입력 문자열을 HTML로 변환하는 필터 함수
@register.filter()
def mark(value):
    #nl2br은 줄바꿈 문자를 <br>, fenced_code는 위에서 살펴본 마크다운으 소스코드 표현을 위해 필요
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))