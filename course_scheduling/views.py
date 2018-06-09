from django.shortcuts import render,render_to_response
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import *
from course_scheduling.models import *
# Create your views here.
def cs_start(request):
    current_group = str(Group.objects.get(user=request.user))
    allclassroom = classroom.objects.filter()
    alllesson = lesson.objects.filter()
    if current_group == 'student':
        return render_to_response('error.html')
    elif current_group == 'teacher':
        username = int(request.user.username)
        if teacher.objects.filter(id = username).exists():
            myteacher = teacher.objects.get(id = username)
            return render_to_response('cs_teacher.html', {'lessons':alllesson, 'myteacher':myteacher})
        else:
            return render_to_response('register_teacher2.html')
    else:
        return render_to_response('cs_mary.html', {'classrooms':allclassroom, 'lessons':alllesson})
def register_teacher(request):

    name = request.POST['name']
    college = request.POST['college']
    id = int(request.user.username)
    newteacher = teacher(name=name,college=college,id=id)
    newteacher.save()
    return HttpResponseRedirect('/course_scheduling/')
def publish_class(request):
    if request.method == 'POST':
        student = int(request.POST['student'])
        time = int(request.POST['time'])
        name = request.POST['name']
        newlesson = lesson(name=name,student_number=student,lesson_hour=time)
        newlesson.save()
        return HttpResponseRedirect('/course_scheduling/')
    else:
        return render_to_response('cs_publish.html')
def add_classroom(request):
    if request.method == 'POST':
        name = request.POST['name']
        capacity = int(request.POST['capacity'])
        location = request.POST['location']
        newclassroom = classroom(name=name, location=location,capacity=capacity)
        newclassroom.save()
        return HttpResponseRedirect('/course_scheduling/')
    else:
        return render_to_response('cs_add.html')
def delete_classroom(request):
    room = classroom.objects.get(id = int(request.POST['id']))
    room.delete()
    return HttpResponseRedirect('/course_scheduling/')
def delete_lesson(request):
    mylesson = lesson.objects.get(id = int(request.POST['id']))
    mylesson.delete()
    return HttpResponseRedirect('/course_scheduling/')
def search(request):
    if request.method=='POST':
        this_teacher = teacher.objects.get(name=str(request.POST['name']))

        all_time = time.objects.filter(teacher=this_teacher)
        return render_to_response('search.html', {'all_time':all_time})
    else:
        return render_to_response('search.html')
def choose_lesson(request):
    option = request.POST.getlist('option')
    lesson_id = int(request.POST['id'])
    this_lession = lesson.objects.get(id = lesson_id)
    this_teacher = teacher.objects.get(id = int(request.user.username))
    classrooms = classroom.objects.filter()
    all_time_for_teacher = time.objects.filter(teacher=this_teacher)
    class Time:
        def __init__(self,week,time):
            self.week=week
            self.time=time
    class Teacher:
        def __init__(self):
            self.time=[]
        def addtime(self,time):
            self.time.append(time)
    ThisTeacher = Teacher()
    for i in all_time_for_teacher:
        NewTime = Time(week=i.week,time=i.time)
        ThisTeacher.addtime(NewTime)
    class ClassRoom:
        def __init__(self,id,size):
            self.id = id
            self.time=[]
            self.size = size
        def addtime(self,time):
            self.time.append(time)
    AllClassRoom = []
    for i in classrooms:
        newclassroom = ClassRoom(size=i.capacity,id=i.id)
        this_room_time = time.objects.filter(classroom=i)
        for j in this_room_time:
            new_time = Time(week=j.week,time=j.time)
            newclassroom.addtime(new_time)
        AllClassRoom.append(newclassroom)

    class Lesson:
        def __init__(self,stunum,teacher):
            self.studentnum = stunum
            self.teacher=teacher
            self.classroom=None
        def addtime(self,time):
            self.time=time
    ThisLesson = Lesson(stunum=this_lession.student_number,teacher=ThisTeacher)

    class Manager:
        def __init__(self,teacher,lesson,options,classrooms):
            self.options = options
            self.teacher=teacher
            self.lesson=lesson
            self.classrooms = classrooms
        def manage(self):
            last_lesson = 0
            last_day = 0
            for time in self.teacher.time:
                if time.week>=last_day:
                    last_day=time.week
                    last_lesson=time.time
            if last_day == 0:
                last_day=1
            if last_lesson == 6 and last_day==5:
                return False
            elif last_lesson==6 and last_day<5:
                last_day+=1
                last_lesson = 1
            else:
                last_lesson += 1
            if '1' in self.options and last_lesson ==1:
                last_lesson = 2
            choosed_classroom = None
            for classroom in self.classrooms:
                CanBeChoose = True
                if classroom.size<self.lesson.studentnum:
                    CanBeChoose = False
                for time in classroom.time:
                    if time.week == last_day and time.time == last_lesson:
                        CanBeChoose = False
                        break
                if CanBeChoose:
                    choosed_classroom = classroom
                    break
                else:
                    continue
            if choosed_classroom != None:
                self.lesson.classroom = choosed_classroom
                newtime = Time(week=last_day,time=last_lesson)
                self.lesson.addtime(newtime)
                self.teacher.addtime(newtime)
                choosed_classroom.addtime(newtime)
            else:
                return False
            return True
    my_manager = Manager(teacher=ThisTeacher,lesson = ThisLesson,classrooms = AllClassRoom,options=option)

    result = my_manager.manage()

    if result == True:
        choosed_classroom = classroom.objects.get(id=int(ThisLesson.classroom.id))
        print (choosed_classroom.name)
        this_lession.room = choosed_classroom
        this_lession.teacher = this_teacher
        this_lession.save()
        add_time = time(week=ThisLesson.time.week,time=ThisLesson.time.time,lesson=this_lession,teacher=this_teacher,classroom=choosed_classroom)
        add_time.save()
    return HttpResponseRedirect('/course_scheduling/')
def check_my_lesson(request):
    this_teacher = teacher.objects.get(id = int(request.user.username))
    all_time = time.objects.filter(teacher=this_teacher)
    return render_to_response('search2.html', {'all_time':all_time})
def lesson_exit(request):
    lessonid = int(request.POST['id'])
    this_lesson = lesson.objects.get(id = lessonid)
    this_lesson.teacher=None
    this_lesson.room=None
    this_time = time.objects.get(lesson=this_lesson)
    this_time.delete()
    this_lesson.save()
    return HttpResponseRedirect('/course_scheduling/')