from django.shortcuts import render,render_to_response
from django.contrib.auth.models import *
from graduation_proj.models import *
from django.http.response import HttpResponseRedirect
# Create your views here.
def graduation_start(request):
    current_group = str(Group.objects.get(user=request.user))
    if current_group == 'student':
        username = int(request.user.username)
        if student.objects.filter(id=username).exists():
            myproject = graduation_project.objects.get(Student=student.objects.get(id = username))
            return render_to_response('graduation_student.html', {'myproject':myproject})
        else:
            return render_to_response('register_student3.html')
    elif current_group == 'teacher':
        username = int(request.user.username)
        if teacher.objects.filter(id=username).exists():
            ThisTeacher = teacher.objects.get(id = username)
            MyProjects = graduation_project.objects.filter(Teacher=ThisTeacher)
            AllProjects = graduation_project.objects.filter(Teacher=None)
            MyJudgeProjects = graduation_project.objects.filter(Judger=ThisTeacher)
            return render_to_response('graduation_teacher.html',{'teacher':ThisTeacher,'projects':MyProjects,'allprojects':AllProjects,'judgeprojects':MyJudgeProjects})
        else:
            return render_to_response('register_teacher3.html')
    else:
        allprojects = graduation_project.objects.filter()
        return render_to_response('graduation_mary.html',{'allprojects':allprojects})
def register_teacher(request):
    id = int(request.user.username)
    name = request.POST['name']
    college = request.POST['college']
    position = request.POST['position']
    newteacher = teacher(id=id,Name=name,College=college,Position=position)
    newteacher.save()
    return HttpResponseRedirect('/graduation_proj/')
def register_student(request):
    id = int(request.user.username)
    name = request.POST['name']
    college = request.POST['college']
    newstudent = student(id=id,Name=name,College=college)
    newstudent.save()
    newproject = graduation_project(Student=newstudent)
    newproject.save()
    return HttpResponseRedirect('/graduation_proj/')
def manage(request):
    id = int(request.POST['project'])
    ThisProject = graduation_project.objects.get(id = id)
    return render_to_response('manage.html',{'project':ThisProject})
def join(request):
    projectid = int(request.POST['project'])
    teacherid = int(request.POST['teacher'])
    thisproject = graduation_project.objects.get(id = projectid)
    thisteacher = teacher.objects.get(id = teacherid)
    thisproject.Teacher=thisteacher
    thisproject.save()
    return HttpResponseRedirect('/graduation_proj/')
def teacher_judge(request):
    id = int(request.POST['project'])
    title = request.POST['name']
    content = request.POST['content']
    newopinion = opinion(TeacherName=title,Content=content)
    newopinion.save()
    this_proj = graduation_project.objects.get(id = id)
    this_proj.TeacherOpinion = newopinion
    this_proj.save()
    return HttpResponseRedirect('/graduation_proj/')
def student_manage(request):
    id = int(request.POST['project'])
    ThisProject = graduation_project.objects.get(id=id)
    return render_to_response('student_manage.html', {'project': ThisProject})
def updateAssignmentBook(request):
    id = int(request.POST['project'])
    thisproject = graduation_project.objects.get(id = id)
    title = request.POST['title']
    content = request.POST['content']
    newreport = report(Title=title,Content=content)
    newreport.save()
    thisproject.AssignmentBook = newreport
    thisproject.save()
    return HttpResponseRedirect('/graduation_proj/')
def updateMiddleReport(request):
    id = int(request.POST['project'])
    thisproject = graduation_project.objects.get(id=id)
    title = request.POST['title']
    content = request.POST['content']
    newreport = report(Title=title, Content=content)
    newreport.save()
    thisproject.MiddleReport = newreport
    thisproject.save()
    return HttpResponseRedirect('/graduation_proj/')
def updateFinalReport(request):
    id = int(request.POST['project'])
    thisproject = graduation_project.objects.get(id=id)
    title = request.POST['title']
    content = request.POST['content']
    newreport = report(Title=title, Content=content)
    newreport.save()
    thisproject.FinalReport = newreport
    thisproject.save()
    return HttpResponseRedirect('/graduation_proj/')
def updateSelectTopic(request):
    id = int(request.POST['project'])
    thisproject = graduation_project.objects.get(id=id)
    title = request.POST['title']
    content = request.POST['content']
    newreport = report(Title=title, Content=content)
    newreport.save()
    thisproject.SelectTopic = newreport
    thisproject.save()
    return HttpResponseRedirect('/graduation_proj/')
def addjudger(request):
    if 'name' in request.POST:
        if teacher.objects.filter(Name=request.POST['name']).exists():
            thisteacher = teacher.objects.get(Name=request.POST['name'])
            thisproject = graduation_project.objects.get(id=int(request.POST['id']))
            thisproject.Judger.add(thisteacher)
        return HttpResponseRedirect('/graduation_proj/')
    else:
        return render_to_response('addjudger.html', {'id':int(request.POST['project'])})
def check(request):
    id = int(request.POST['id'])
    thisproject = graduation_project.objects.get(id = id)
    return render_to_response('check.html',{'project':thisproject})
def manage2(request):
    id = int(request.POST['project'])
    ThisProject = graduation_project.objects.get(id=id)
    return render_to_response('manage2.html', {'project': ThisProject})
def judger_judge(request):
    id = int(request.POST['project'])
    title = request.POST['name']
    content = request.POST['content']
    newopinion = opinion(TeacherName=title, Content=content)
    newopinion.save()
    this_proj = graduation_project.objects.get(id=id)
    this_proj.JudgerOpinion = newopinion
    this_proj.save()
    return HttpResponseRedirect('/graduation_proj/')