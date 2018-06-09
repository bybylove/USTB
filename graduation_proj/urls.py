from django.urls import path
from graduation_proj.views import *
urlpatterns = [
    path('',graduation_start),
    path('register_teacher/',register_teacher),
    path('register_student/',register_student),
    path('manage/',manage),
    path('manage2/',manage2),
    path('join/',join),
    path('manage/teacher_judge/',teacher_judge),
    path('manage2/judger_judge/',judger_judge),
    path('student_manage/',student_manage),
    path('student_manage/updateAssignmentBook/',updateAssignmentBook),
    path('student_manage/updateMiddleReport/',updateMiddleReport),
    path('student_manage/updateFinalReport/',updateFinalReport),
    path('student_manage/updateSelectTopic/',updateSelectTopic),
    path('addjudger/',addjudger),
    path('check/',check),
]