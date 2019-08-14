# django imports style guide
# 1. standard library
# 2. third-party
# 3. django
# 4. local django
import random
from datetime import datetime
from django.shortcuts import render


# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html',) # render() 의 첫번째 인자도 반드시 request


def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'introduce.html', context)


def dinner(request):
    menu = ['소불고기', '잡채덮밥', '나주곰탕']
    pick = random.choice(menu)
    context = {'pick': pick,}
    return render(request, 'dinner.html', context)


def image(request):
    return render(request, 'image.html')


def hello(request, name):
    menu = ['소불고기', '잡채덮밥', '나주곰탕']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,}
    return render(request, 'hello.html', context)


def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num3': num3,}
    return render(request, 'times.html', context)


def area(request, r):
    area = r**2*3.14
    context = {'r': r, 'area': area,}
    return render(request, 'area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'isitgwangbok.html', context)