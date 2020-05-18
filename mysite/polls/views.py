from .models import Question, Choice
from django.urls import reverse
# {①に必要、②はいらない}
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# {②に必要、①はいらない}
from django.shortcuts import render, redirect, get_object_or_404
# {汎用ビューを使う時}
from django.views import generic


# {汎用ビューを使う時のクラス設定}
# 重要・・・そもそもListViewはオブジェクトに対するリスト
#           そしてDetailViewはオブジェクトの中身に対するアプローチなので、例え結果という一覧（リスト）があったとしてもそれはあくまでオブジェクトであるquestionの詳細情報ということになるから、その際はDetailViewを使うのである。

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    
    context_object_name = 'latest_question_list'
    # これを使っている理由は、ListViewの自動生成の変数が使用モデル名_listになるが、自分で自由に変数名を設定する為にcontext_object_nameを使って設定していて、そのおかげで、ビューのlatest_question_listを変更せずに使える。これを設定しなかったら、ビューのlatest_question_listをquestion_listにすれば一応使える。

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):#この時点で下で設定するモデルの詳細ページを表示するという意味になる
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  #なぜリザルトなのにgeneric.DetailViewを使っているかと言うと、genericつまり汎用ビューのヘルパーの機能として、ListViewとDetail.viewがある。そしてリザルトというのはあるモデルに対しての詳細内容に含まれるから使っているという解釈

    model = Question
    template_name = 'polls/results.html'

# def vote(request, question_id):
#     ... # same as above, no changes needed.


# {汎用ビューを使う際には全部消して大丈夫}
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
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question dose not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POSTではキーを指定すると、送信したデータにアクセスできる。request.POST[choice]は選択された選択肢のIDを文字列として返す。
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        #choiceカウントを１増やした後に、どっか指定の場所に飛ばす際にはリダイレクトを使うので、Httpレスポンスを返すのではなく、Httpレスポンスリダイレクトを返す。
        #argsは引数を意味しpolls/resultsがどの質問に対してのリザルトページに行けば良いのかを指定してあげている。
        # リバース関数が何をしているのかというと、リバース関数内にURLパターンに設定したnameを使ってやると、返り値としてURLを返してくれるというもの。今回で言えば、明示的にpollsのどのリザルト画面に行けば良いかを示すための組み合わせをしていると考えてみよう。


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s" % question_id)
# detail アクションが起こったら、リクエストで指定されたIdを見つけて
# return内容を表示しなさい的な意味であってるはず
