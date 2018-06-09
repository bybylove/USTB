from django.shortcuts import render,render_to_response
from SRTP.models import *
from django.contrib.auth.models import *
from django.http.response import *
import datetime
# Create your views here.
def srtpstart(request):
    current_group = str(Group.objects.get(user = request.user))
    if current_group == 'student':
        username = int(request.user.username)
        if student.objects.filter(id=username).exists():
            srtps = srtp.objects.filter(team=None)
            myteam = student.objects.get(id = int(request.user.username)).team
            mysrtps = srtp.objects.filter(team=myteam)
            return render_to_response('form pro_student.html', {'srtps': srtps, 'team':myteam, 'mysrtps':mysrtps})
        else:
            return render_to_response('register_student.html')
    elif current_group == 'teacher':
        username = int(request.user.username)
        if teacher.objects.filter(id = username).exists():
            myteacher = teacher.objects.get(id = username)
            srtps = srtp.objects.filter(teacher = myteacher)
            return render_to_response('form pro_teacher.html', {'srtps':srtps})
        else:
            return render_to_response('register_teacher.html')
    else:
        mysrtps = srtp.objects.filter()
        myteams = team.objects.filter()
        mystudents = student.objects.filter()
        return render_to_response('form pro-mary.html', {"mysrtps":mysrtps, "myteams":myteams, "mystudents":mystudents})
def srtp_publish(request):
    if request.method == 'POST':
        this_teacher = teacher.objects.get(id = int(request.user.username))
        new_srtp = srtp(name= request.POST['pname'],teacher = this_teacher)
        new_srtp.save()
        return HttpResponseRedirect('/srtp/')
    else:
        return render_to_response('srtp_publish.html')
def register_teacher(request):
    id = int(request.user.username)
    name = request.POST['name']
    college = request.POST['college']
    position = request.POST['position']
    newteacher = teacher(id=id,name=name,college=college,position=position)
    newteacher.save()
    return HttpResponseRedirect('/srtp/')
def register_student(request):
    id = int(request.user.username)
    name = request.POST['name']
    college = request.POST['college']
    newstudent = student(id=id,name=name,college=college)
    newstudent.save()
    return HttpResponseRedirect('/srtp/')
def teacher_delete(request):
    id = int(request.POST['id'])
    srtp.objects.get(id = id).delete()
    return HttpResponseRedirect('/srtp/')
def team_join(request):
    srtp_id = request.POST['srtp']
    team_id = request.POST['team']

    my_srtp = srtp.objects.get(id = int(srtp_id))
    my_team = team.objects.get(id = int(team_id))
    my_srtp.team = my_team
    my_srtp.start_time = datetime.datetime.now()
    my_srtp.save()
    return  HttpResponseRedirect('/srtp/')
def create_team(request):
    if request.method == 'POST':
        team_name = request.POST['name']
        if team.objects.filter(name=team_name).exists():
            return render_to_response('srtp_create_team.html', {'error': '队伍已存在'})
        else:
            this_student = student.objects.get(id = int(request.user.username))
            newteam = team(name=team_name,college=str(this_student.college))
            newteam.save()
            this_student.team = newteam
            this_student.save()
            return HttpResponseRedirect('/srtp/')
    else:
        return render_to_response('srtp_create_team.html')
def join_team(request):
    if request.method == 'POST':
        team_name = request.POST['name']
        if team.objects.filter(name=team_name).exists():
            myteam = team.objects.get(name=team_name)
            me = student.objects.get(id = int(request.user.username))
            me.team = myteam
            me.save()
            return HttpResponseRedirect('/srtp/')
        else:
            return render_to_response('srtp_create_team.html', {'error': '队伍不存在'})
    else:
        return render_to_response('srtp_join_team.html')
def srtp_manage(request):
    this_srtp_id = request.POST['srtp']
    this_srtp = srtp.objects.get(id = int(this_srtp_id))
    return render_to_response('srtp_manage.html', {'srtp':this_srtp})
def ask_money(request):
    money = request.POST['askmoney']
    mysrtp = srtp.objects.get(id = int(request.POST['srtp']))
    mysrtp.money = money
    mysrtp.save()
    return HttpResponseRedirect('/srtp/')
def updatereport(request):
    middle = report(title=request.POST['middlereport_title'],content=request.POST['middlereport'])
    fianl = report(title=request.POST['finalreport_title'],content=request.POST['finalreport'])
    middle.save()
    fianl.save()
    mysrtp = srtp.objects.get(id = int(request.POST['srtp']))
    mysrtp.middle_report =  middle
    mysrtp.final_report = fianl

    mysrtp.save()
    return HttpResponseRedirect('/srtp/')
def srtp_look(request):
    this_srtp_id = request.POST['srtp']
    this_srtp = srtp.objects.get(id = int(this_srtp_id))
    return render_to_response('srtp_look.html', {'srtp':this_srtp})