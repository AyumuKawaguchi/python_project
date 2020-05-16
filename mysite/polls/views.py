from django.http import HttpResponse
from .models import Question
# from django.views.generic import TemplateView
# from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# テンプレート呼び出し
# class IndexView(TemplateView):
#     template_name = "index.html"

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
# detail アクションが起こったら、リクエストで指定されたIdを見つけて
# return内容を表示しなさい的な意味であってるはず

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


