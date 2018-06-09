from django.urls import path
from course_scheduling.views import *
urlpatterns = [
    path('', cs_start),
    path('publish/',publish_class),
    path('add/',add_classroom),
    path('search/',search),
    path('classroom_delete/',delete_classroom),
    path('lesson_delete/',delete_lesson),
    path('choose_lesson/',choose_lesson),
    path('register_teacher/',register_teacher),
    path('check_my_lesson/',check_my_lesson),
    path('lesson_exit/',lesson_exit),
]