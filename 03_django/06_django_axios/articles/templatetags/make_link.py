from django import template

register = template.Library()   # 기존 템플릿 라이브러리에

@register.filter
def hashtag_link(word):
    # word는 article 객체가 들어갈건데
    # article의 content 들만 모두 가져와서 그 중 해시태그에만 링크를 붙인다.
    content = word.content + ' ' # 공백포함 내용 저장
    hashtags = word.hashtags.all() # word가 가지는 hashtag전부 가져옴

    # 기존 hashtag들을 링크로 바꾼다!
    for hashtag in hashtags:
        content = content.replace(hashtag.content + ' ', f'<a href="/articles/{hashtag.pk}/hashtag/">{ hashtag.content }</a> ')  # a tag 이후 마지막 공백 주의! # .replace(과거내용, html a태그를 씌운 hashtag.content + ' ')

    return content