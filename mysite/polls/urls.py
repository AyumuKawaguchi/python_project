from django.urls import path

from . import views

app_name = 'polls'
# これを設定することでプロジェクト内のどのアプリを使用しているか、ひいてはどのアプリのビューを使うかを定める。これを名前空間という。

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]