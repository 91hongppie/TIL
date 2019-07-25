# 190725 workshop2

```python
from flask import Flask
app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    word_book = {
        'apple': '사과',
        'banana': '바나나'
    }
    
    if word in word_book:
        result = f'{word}는 {word_book.get(word)}'
    else:
        result = f'{word}은(는) 나만의 단어장에 없는 단어입니다!'
    return result
```

