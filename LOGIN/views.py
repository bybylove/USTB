from django.shortcuts import render
from django.contrib import auth
from django.http.request import *
from django.http.response import *
from LOGIN.models import *
import re
import urllib.request
# Create your views here.
from django.shortcuts import render_to_response
def login(request):
    urlandnametodelete = urlandname.objects.filter()
    for i in urlandnametodelete:
        i.delete()
    url = "http://teach.ustb.edu.cn"
    response = urllib.request.urlopen(url=url)
    result = response.read().decode('gb2312')
    regex = re.compile(r'''<A\shref=(bencandy.php\?.*?)\starget=_blank>(.*?)</A>''')
    match = regex.findall(result)
    for i in match:
        x = "http://teach.ustb.edu.cn/"+i[0]
        y = i[1]
        newurlandname = urlandname(url = x,name=y)
        newurlandname.save()
    allurlandname = urlandname.objects.filter()
    if request.user.is_authenticated:
        return render_to_response('login_in.html',{'urlandname':allurlandname})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is None:
            return render_to_response('login.html',{'error':'输入有误!'})
        else:
            auth.login(request,user)
            return render_to_response('login_in.html',{'urlandname':allurlandname})
    return render_to_response('login.html')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect('/')
def setting(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST['password']==request.POST['password2']:
            if request.POST['password'] == request.POST['password2'] and request.user.check_password(request.POST['oldpassword']):
                user = request.user
                user.set_password(request.POST['password'])
                user.save()
            return render_to_response('login.html',{'error':'请重新登录'})
        else:
            return render_to_response('setting.html')
    else:
        return render_to_response('login.html',{'error':'请先登录!'})
