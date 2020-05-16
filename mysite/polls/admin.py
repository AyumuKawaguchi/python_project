from django.contrib import admin

from .models import Question
# adminにモデルからquestionモデルを転送するよって感じ
admin.site.register(Question)
# これないと表示が出ない