from django.urls import path
from SRTP.views import *
urlpatterns = [
    path('',srtpstart),
    path('publish/',srtp_publish),
    path('register_teacher/',register_teacher),
    path('register_student/',register_student),
    path('teacher_delete/',teacher_delete),
    path('team_join/',team_join),
    path('create_team/',create_team),
    path('join_team/',join_team),
    path('srtp_manage/',srtp_manage),
    path('srtp_manage/askmoney/',ask_money),
    path('srtp_manage/updatereport/',updatereport),
    path('srtp_look/',srtp_look),
]