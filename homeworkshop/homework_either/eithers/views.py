from django.shortcuts import render, redirect
from .models import Question, Answer
# Create your views here.

def index(request):
    questions = Question.objects.order_by('-pk')
    context = {'questions': questions,}
    return render(request, 'eithers/index.html', context)

def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        issue_a = request.POST.get('issue_a')
        issue_b = request.POST.get('issue_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')
        question = Question(title=title, issue_a=issue_a, issue_b=issue_b, image_a=image_a, image_b=image_b)
        question.save()

        return redirect('question:index')
    else:
        return render(request, 'eithers/new.html')

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    answers = question.answer_set.all()
    cnt = cnt1 = 0
    per_1 = per_2 = 0
    for answer in answers:
        cnt += 1
        if answer.pick:
            cnt1 += 1
    if cnt:
        per_1 = (cnt1/cnt)*100
        per_2 = (1-cnt1/cnt)*100
    context = {'question': question, 'answers': answers, 'per_1': per_1, 'per_2': per_2,}
    return render(request, 'eithers/detail.html', context)

def answers_create(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        content = request.POST.get('answer')
        pick = request.POST.get('pick')
        comment = Answer(question=question, pick=pick, comment=content,)
        comment.save()
        return redirect('question:detail', question_pk)
    else:
        return redirect('question:detail', question_pk)

def answers_delete(request, question_pk, answer_pk):
    comment = Answer.objects.get(pk=answer_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('question:detail', question_pk)
