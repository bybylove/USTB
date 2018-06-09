from django.urls import path
from PM.views import *
urlpatterns = [
    path('',pmstart),
    path('look/',look),
    path('publish/',publish),
    path('manage_mary/',manage),
    path('manage_mary/addmoneyrecord',addmoneyrecord),
    path('manage_mary/addmiddle',addmiddle),
    path('manage_mary/addresult',addresult),
    path('manage_mary/addcheck',addcheck),
    path('manage_mary/addarchievement',addarchievement),

]