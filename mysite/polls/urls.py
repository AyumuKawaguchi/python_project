from django.urls import path

from . import views

app_name = 'polls'
# これを設定することでURLパターンにapp名を記載できるようになりプロジェクト内のどのアプリを使用しているか、ひいてはどのアプリのビューを使うかを定める。これを名前空間という。

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #汎用ビューの決まりなので覚えるしかないが、idを汎用ビューで使用する為にはpkと言うものに置き換えるものとして覚える。

    # ex: /polls/5/results
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]