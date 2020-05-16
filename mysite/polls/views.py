from .models import Question

# {①に必要、②はいらない}
from django.http import HttpResponse
from django.template import loader
# {②に必要、①はいらない}
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # データベースからquestionのオブジェクトを発表順に5つまで表示する
    # output = ', '.join([q.question_text for q in latest_question_list])
    #変数qというのはここではlatest_question_listから取り出した1つ1つの要素のこと
    #変数qにlatest_question_listから1つずつオブジェクトを取り出してオブジェクトの質問のテキストをカンマ区切りで表示するということ。
    # return HttpResponse(output)

# {①が必要}
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template =  loader.get_template('polls/index.html')
    # context = {'latest_question_list': latest_question_list,}
    # return HttpResponse(template.render(context, request))
# {②が必要}
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
# detail アクションが起こったら、リクエストで指定されたIdを見つけて
# return内容を表示しなさい的な意味であってるはず

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


