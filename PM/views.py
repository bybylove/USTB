from django.shortcuts import render , render_to_response
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import *
from PM.models import *
import datetime
# Create your views here.
def pmstart(request):
    current_group = str(Group.objects.get(user=request.user))
    allproject = project.objects.filter()
    if current_group == 'student' or current_group == 'teacher':
        return render_to_response('pmatart.html',{'allpriject':allproject})
    else:
        return render_to_response('pmstart_mary.html',{'allpriject':allproject})
def look(request):
    id = int(request.POST['id'])
    thisproject = project.objects.get(id = id)
    return render_to_response('look.html',{'inform':thisproject.inform})
def publish(request):
    if request.method == 'POST':
        name = request.POST['name']
        type = request.POST['type']
        inform = request.POST['inform']
        newproject = project(name=name,type=type,inform=inform)
        newproject.save()
        return HttpResponseRedirect('/pm/')
    else:
        return render_to_response('publish.html')
def manage(request):
    id = int(request.POST['id'])
    thisproject = project.objects.get(id = id )
    thismoney = money.objects.filter(proj=thisproject)
    thischeck = check.objects.filter(proj=thisproject)
    thisarchievement = archievement.objects.filter(proj=thisproject)
    return render_to_response('manage_mary.html',{'project':thisproject,'check':thischeck,'money':thismoney,'archievement':thisarchievement})
def addmoneyrecord(request):
    quantity = int(request.POST['quantity'])
    id = int(request.POST['id'])
    detail = request.POST['detail']

    thisproject = project.objects.get(id = id)
    newmoney = money(quantity=quantity, detail=detail,proj=thisproject)
    newmoney.save()
    return HttpResponseRedirect('/pm/')
def addmiddle(request):
    middle = request.POST['middle']
    id = int(request.POST['id'])
    thisproject = project.objects.get(id = id )
    thisproject.middle = middle
    thisproject.save()
    return HttpResponseRedirect('/pm/')
def addresult(request):
    result = request.POST['result']
    id = int(request.POST['id'])
    thisproject = project.objects.get(id=id)
    thisproject.result = result
    thisproject.save()
    return HttpResponseRedirect('/pm/')
def addcheck(request):
    now = datetime.datetime.now()
    log = request.POST['log']
    id = int(request.POST['id'])
    thisproject = project.objects.get(id = id )
    newcheck = check(log=log,date=now,proj=thisproject)
    newcheck.save()
    return HttpResponseRedirect('/pm/')
def addarchievement(request):
    type = request.POST['type']
    detail = request.POST['detail']
    id = int(request.POST['id'])
    thisproject = project.objects.get(id=id)
    newcheck = archievement(type=type, detail=detail, proj=thisproject)
    newcheck.save()
    return HttpResponseRedirect('/pm/')